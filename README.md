# Multilingual AI Research Assistant

This project provides a multilingual AI research assistant that helps users get answers to research-related queries in various languages. The system leverages the power of arXiv research papers, language translation, and advanced LLMs (Cohere in this case) to answer questions based on the research papers. It supports multiple languages for both input queries and output answers.

## Features

*   **Multilingual Support:** Ask your research query in multiple languages and get answers in any language of your choice.
*   **Research Query Handling:** The system performs an arXiv search based on your research query and uses relevant research papers to generate answers.  Multiple queries can be provided, separated by the word "OR".
*   **Answer Generation:** Uses a retrieval-based question-answering mechanism with LLMs to generate answers based on the retrieved context.
*   **Translation:** The system translates queries and answers between various languages, ensuring a smooth experience for users who prefer different languages.

## Deployment

You can access the deployed interface on [Hugging Face Spaces](https://huggingface.co/spaces/KartikGarg163/Multilingual-AI-Research-Assistant?logs=container).

## Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/KartikGarg20526/Multilingual-AI-Research-Assistant.git](https://www.google.com/search?q=https://github.com/KartikGarg20526/Multilingual-AI-Research-Assistant.git)
    cd Multilingual-AI-Research-Assistant
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

    You need to set the `COHERE_API_KEY` environment variable for Cohere's LLM API. You can get the API key from [Cohere](https://cohere.com/).

    *   **Linux/macOS:**

        ```bash
        export COHERE_API_KEY="your_cohere_api_key"
        ```

    *   **Windows:**

        ```bash
        set COHERE_API_KEY=your_cohere_api_key
        ```

5.  **Run the Gradio interface:**

    ```bash
    python app.py
    ```

## How to Use

1.  **Research Query:** Enter your research query in the "Research Query" textbox.  Separate multiple queries with the word "OR".
2.  **Question:** Ask a question related to the research papers based on the query.
3.  **Input Language:** Choose the language you want to input your query in.
4.  **Output Language:** Choose the language in which you want the answer to be provided.
5.  **Submit:** Click the "Submit" button to get an answer to your question based on the research papers related to the query.

## Technologies Used

*   **arXiv:** To search for relevant research papers.
*   **Argos Translate:** For language translation.
*   **Cohere LLM:** For generating answers based on the retrieved context from the papers.
*   **Gradio:** For building the interactive web interface.
*   **LangChain:** For handling document processing, vector databases, and question answering chains.
