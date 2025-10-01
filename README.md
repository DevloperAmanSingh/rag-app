# RAG Chat

A modern Retrieval-Augmented Generation (RAG) application built with Streamlit and LLMWare. Upload documents, generate embeddings, and ask questions with AI-powered answers and source attribution.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- 4GB+ RAM (for model loading)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd code-review-bot

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎯 Features

### Document Management

- **Upload Files**: Drag & drop PDF, TXT, DOCX files
- **Local Folder**: Point to a directory with documents
- **Sample Data**: Use LLMWare's sample invoice dataset

### AI-Powered Search

- **Semantic Search**: Find relevant documents using vector embeddings
- **Source Attribution**: See which documents were used for answers
- **Context-Aware**: Answers are based on your specific documents

### Technical Features

- **Vector Database**: Uses Milvus for efficient similarity search
- **Embedding Model**: `industry-bert-contracts` for document understanding
- **LLM Model**: `bling-phi-3-gguf` for generating responses
- **Session State**: Maintains state across interactions

## 🔧 How It Works

### 1. Document Processing

```python
# Create a library and add documents
library = Library().create_new_library("MyDocs")
library.add_files("/path/to/documents")
```

### 2. Embedding Generation

```python
# Generate vector embeddings for semantic search
library.install_new_embedding(
    embedding_model_name="industry-bert-contracts",
    vector_db="milvus"
)
```

### 3. Query Processing

```python
# Search for relevant documents
query_results = Query(library).semantic_query(question, result_count=5)

# Generate AI response with context
prompter = Prompt().load_model("bling-phi-3-gguf")
response = prompter.prompt_with_source(question)
```

## 📊 Usage Examples

### Upload and Query Documents

1. **Load Documents**: Choose "Upload files" and select your PDFs
2. **Generate Embeddings**: Click "Generate Embeddings" (one-time setup)
3. **Ask Questions**: Enter questions like:
   - "What is the total amount of the invoice?"
   - "Who is the vendor for invoice #12345?"
   - "What are the payment terms?"

### Sample Questions for Invoice Documents

- "What is the total amount due?"
- "When is the payment due date?"
- "Who is the customer on this invoice?"
- "What services were provided?"

## 🔍 Technical Details

### Dependencies

- **Streamlit**: Web UI framework
- **LLMWare**: RAG and document processing
- **Milvus**: Vector database for embeddings
- **HuggingFace**: Model hosting and downloads

### Model Information

- **Embedding Model**: `industry-bert-contracts` (optimized for business documents)
- **LLM Model**: `bling-phi-3-gguf` (2.4GB, requires sufficient RAM)
- **Vector DB**: Milvus (local, no external dependencies)

---

**Built with ❤️ using Streamlit and LLMWare**
