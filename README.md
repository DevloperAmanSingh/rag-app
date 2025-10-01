# RAG Chat

## 🚀 Quick Start

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

### Technical Features

- **Vector Database**: Uses Milvus for efficient similarity search
- **Embedding Model**: `industry-bert-contracts` for document understanding
- **LLM Model**: `bling-phi-3-gguf` for generating responses

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

## 🔍 Technical Details

### Dependencies

- **Streamlit**: Web UI framework
- **LLMWare**: RAG and document processing
- **Milvus**: Vector database for embeddings
- **HuggingFace**: Model hosting and downloads


