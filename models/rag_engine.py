import os
import tempfile
from typing import List, Dict, Optional

from llmware.library import Library
from llmware.retrieval import Query
from llmware.prompts import Prompt
from llmware.setup import Setup


class RAGEngine:
    
    def __init__(self):
        self.library: Optional[Library] = None
        self.embeddings_ready = False
    
    def create_library_from_uploads(self, uploaded_files) -> bool:
        try:
            temp_dir = tempfile.mkdtemp()
            for uploaded_file in uploaded_files:
                with open(os.path.join(temp_dir, uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
            
            self.library = Library().create_new_library("UploadedDocs")
            self.library.add_files(temp_dir)
            return True
        except Exception as e:
            print(f"Error creating library from uploads: {e}")
            return False
    
    def create_library_from_folder(self, folder_path: str) -> bool:
        try:
            self.library = Library().create_new_library("LocalDocs")
            self.library.add_files(folder_path)
            return True
        except Exception as e:
            print(f"Error creating library from folder: {e}")
            return False
    
    def create_library_from_samples(self) -> bool:
        try:
            sample_files_path = Setup().load_sample_files(over_write=False)
            doc_path = os.path.join(sample_files_path, "Invoices")
            self.library = Library().create_new_library("SampleInvoices")
            self.library.add_files(doc_path)
            return True
        except Exception as e:
            print(f"Error creating library from samples: {e}")
            return False
    
    def generate_embeddings(self) -> bool:
        if not self.library:
            return False
        
        try:
            self.library.install_new_embedding(
                embedding_model_name="industry-bert-contracts", 
                vector_db="milvus"
            )
            self.embeddings_ready = True
            return True
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            return False
    
    def query_documents(self, question: str, model_name: str = "bling-phi-3-gguf") -> Dict:
        if not self.library or not self.embeddings_ready:
            return {"error": "Library not ready or embeddings not generated"}
        
        try:
            # Perform semantic search
            query_results = Query(self.library).semantic_query(question, result_count=5)
            
            # Load model and generate response
            prompter = Prompt().load_model(model_name, temperature=0.0, sample=False)
            sources = prompter.add_source_query_results(query_results)
            
            response = prompter.prompt_with_source(question)
            
            return {
                "success": True,
                "response": response,
                "query_results": query_results
            }
        except Exception as e:
            return {"error": f"Query failed: {str(e)}"}
    
    def get_library_status(self) -> Dict:
        return {
            "has_library": self.library is not None,
            "embeddings_ready": self.embeddings_ready
        }
