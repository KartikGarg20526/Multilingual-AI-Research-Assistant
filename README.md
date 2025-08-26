# Multilingual AI Research Assistant

## 🔬 About

The **Multilingual AI Research Assistant** is an intelligent research companion that bridges language barriers in academic research. By leveraging the power of arXiv research papers, advanced language translation, and Large Language Models (Cohere), it enables researchers worldwide to:

- **Query in their native language** and receive answers in any preferred language
- **Access cutting-edge research** from arXiv's vast repository of academic papers
- **Get contextually relevant answers** powered by retrieval-augmented generation (RAG)
- **Break down language barriers** in academic research and collaboration

Perfect for researchers, students, academics, and anyone seeking multilingual access to scientific literature.

## ✨ Features

### 🌍 **Multilingual Support**
- **Input**: Ask questions in 10+ languages (English, Spanish, French, German, Italian, Russian, Chinese, Japanese, Korean, Hindi)
- **Output**: Receive answers in any supported language
- **Smart Translation**: Powered by Argos Translate for accurate academic terminology

### 📚 **Intelligent Research Processing**
- **arXiv Integration**: Automatically searches and processes relevant research papers
- **Advanced Query Handling**: Support for complex queries with OR operators
- **Document Processing**: Extracts and processes PDF content from research papers
- **Context-Aware Answers**: Uses RAG (Retrieval-Augmented Generation) for precise responses

### 🤖 **AI-Powered Analysis**
- **Cohere LLM Integration**: Advanced language model for generating research insights
- **Vector Database**: Efficient document retrieval using Qdrant
- **Semantic Search**: Find relevant information across multiple papers simultaneously

### 🖥️ **User-Friendly Interface**
- **Gradio Web Interface**: Clean, intuitive web application
- **Real-time Processing**: Get answers in seconds
- **Responsive Design**: Works seamlessly across devices

## 🎥 Demo

**Live Demo**: [Access on Hugging Face Spaces](https://huggingface.co/spaces/KartikGarg163/Multilingual-AI-Research-Assistant)

### Example Queries

```
Research Query: "machine learning transformers OR neural networks"
Question: "What are the latest improvements in transformer architecture?"
Input Language: English
Output Language: Spanish
```

```
Research Query: "quantum computing algorithms"  
Question: "¿Cuáles son los principales desafíos en los algoritmos cuánticos?"
Input Language: Spanish
Output Language: English
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Cohere API key ([Get one here](https://cohere.ai/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KartikGarg20526/Multilingual-AI-Research-Assistant.git
   cd Multilingual-AI-Research-Assistant
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux  
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   ```bash
   # Linux/macOS
   export COHERE_API_KEY="your_cohere_api_key_here"
   
   # Windows Command Prompt
   set COHERE_API_KEY=your_cohere_api_key_here
   
   # Windows PowerShell
   $env:COHERE_API_KEY="your_cohere_api_key_here"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the interface**
   Open your browser and go to the local URL displayed in the terminal (typically `http://127.0.0.1:7860`)

## 📖 Usage

### Basic Workflow

1. **Enter Research Query**: Specify your research topic(s). Use "OR" to separate multiple queries
   - Example: `"natural language processing OR NLP transformers"`

2. **Ask Your Question**: Pose a specific question about your research area
   - Example: `"What are the main challenges in multilingual NLP?"`

3. **Choose Languages**: Select your input and output languages from the dropdown menus

4. **Get Your Answer**: Click Submit and receive a comprehensive, research-backed response

### Advanced Usage Tips

- **Complex Queries**: Use OR operators to broaden your search scope
- **Specific Questions**: Be specific in your questions for more targeted answers
- **Language Mixing**: Input in one language, get output in another for cross-cultural research
- **Academic Context**: The system is optimized for academic and research-oriented queries

## 🏗️ Architecture

The application follows a modular architecture:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Gradio UI     │    │  Translation     │    │   arXiv API     │
│                 │───▶│  (Argos)         │───▶│                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Cohere LLM     │◄───│  RAG Pipeline    │◄───│ Document        │
│                 │    │  (LangChain)     │    │ Processing      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  Vector Store    │
                       │  (Qdrant)        │
                       └──────────────────┘
```

## 🛠️ Technologies Used

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI/ML** | [Cohere LLM](https://cohere.ai/) | Answer generation and reasoning |
| **Translation** | [Argos Translate](https://github.com/argosopentech/argos-translate) | Multi-language support |
| **Research API** | [arXiv Python](https://github.com/lukasschwab/arxiv.py) | Academic paper retrieval |
| **RAG Framework** | [LangChain](https://langchain.com/) | Document processing and retrieval |
| **Vector Database** | [Qdrant](https://qdrant.tech/) | Semantic search and storage |
| **Embeddings** | [HuggingFace Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | Text vectorization |
| **PDF Processing** | [PyPDF](https://github.com/py-pdf/pypdf) | Document parsing |
| **Web Interface** | [Gradio](https://gradio.app/) | Interactive UI |

## 📋 API Reference

### Supported Languages

| Language | ISO Code | Language | ISO Code |
|----------|----------|----------|----------|
| English | `en` | Chinese | `zh` |
| Spanish | `es` | Japanese | `ja` |
| French | `fr` | Korean | `ko` |
| German | `de` | Hindi | `hi` |
| Italian | `it` | Russian | `ru` |

### Query Format

- **Single Query**: `"machine learning"`
- **Multiple Queries**: `"deep learning OR neural networks OR AI"`
- **Complex Queries**: `"transformer architecture OR attention mechanisms OR BERT"`

