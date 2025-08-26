import arxiv
import os
import argostranslate.translate
import argostranslate.package
import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.llms import Cohere
from langchain_huggingface import HuggingFaceEmbeddings

cohere_api_key = os.environ.get('COHERE_API_KEY')

LANGUAGE_ISO_CODES = {
    'Korean': 'ko',
    'German': 'de',
    'Hindi': 'hi',
    'Italian': 'it',
    'Spanish': 'es',
    'Russian': 'ru',
    'Chinese': 'zh',
    'English': 'en',
    'Japanese': 'ja',
    'French': 'fr'
}

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

# Translating text
def translate_text(text, from_code, to_code):
    try:
        package_to_install = next(filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages))
        argostranslate.package.install_from_path(package_to_install.download())
        translated_text = argostranslate.translate.translate(text, from_code, to_code)
        return translated_text
    except Exception as e:
        print("Error in translate_text: ", e)


def process_papers_text(query, input_language='English'):
    input_lang_code = LANGUAGE_ISO_CODES[input_language]
    query_in_english = translate_text(query, from_code=input_lang_code, to_code="en") if input_language != "English" else query
    
    # Search arXiv for papers related to query
    client = arxiv.Client()
    search = arxiv.Search(
        query=query_in_english,
        max_results=5,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    # Download papers and read the text
    full_text = ""
    for result in client.results(search):
        while True:
            try:
                pdf_path = result.download_pdf()
                loader = PyPDFLoader(pdf_path)
                papers = loader.load()
                for pages in papers:
                    full_text += pages.page_content
                break
            except Exception as e:
                print("Error occurred:", e)
    
    return full_text


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_database(text):
    sentences = text.splitlines()
    text = ' '.join(sentences)
    text = text.strip()
    text = ' '.join(text.split())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    paper_chunks = text_splitter.create_documents([text])

    qdrant = Qdrant.from_documents(
        documents=paper_chunks,
        embedding=embeddings,
        location=":memory:",
        collection_name="arxiv_papers",
    )

    return qdrant


prompt_template = """Answer the question based only on the following context:
{context}

Question: {input}
"""

def retrieve_answer_question(question, retriever, input_language='English', output_language='English'):
    try:
        input_lang_code = LANGUAGE_ISO_CODES[input_language]
        output_lang_code = LANGUAGE_ISO_CODES[output_language]

        question_in_english = translate_text(question, from_code=input_lang_code, to_code="en") if input_language != "English" else question
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "input"])
        llm = Cohere(model="command", temperature=0, cohere_api_key=cohere_api_key, max_tokens=2048)
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        chain = create_retrieval_chain(retriever, question_answer_chain)

        answer = chain.invoke({"input": question_in_english})
        result = answer['answer']
        answer_in_output_language = translate_text(result, from_code="en", to_code=output_lang_code) if output_language != "English" else result
        return answer_in_output_language
    except Exception as e:
        return ("Error, Please Try Again.")



def final_setup(query, question, input_language, output_language):
    text = process_papers_text(query, input_language)
    qdrant = create_vector_database(text)
    retriever = qdrant.as_retriever(search_kwargs={"k": 7})
    return retrieve_answer_question(question,retriever,input_language,output_language)


def setup_gradio_interface():
    return gr.Interface(
        fn = lambda query, question, input_language, output_language: final_setup(query, question, input_language, output_language),
        inputs=[
            gr.Textbox(lines=2, placeholder="Enter your Research Query, seperate with 'OR' for multiple queries", label="Research Query"),
            gr.Textbox(lines=2, placeholder="Enter your Question here", label="Question"),
            gr.Dropdown(list(LANGUAGE_ISO_CODES.keys()), label="Input Language"),
            gr.Dropdown(list(LANGUAGE_ISO_CODES.keys()), label="Output Language")
        ],
        outputs="text",
        title="Multilingual AI Research Assistant",
        description="Ask questions on your research query in your chosen language and get an answer in the language of your choice."
    )

iface = setup_gradio_interface()

iface.launch()
