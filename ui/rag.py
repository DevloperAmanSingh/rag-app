import streamlit as st
from models.rag_engine import RAGEngine
from ui.document_loader import render_document_loader, render_embedding_generator
from ui.query_interface import render_query_interface, render_status_info


def render_rag_analyzer() -> None:
    st.title("RAG Chat")

    if "rag_engine" not in st.session_state:
        st.session_state.rag_engine = RAGEngine()

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📁 Load Documents")
        render_document_loader(st.session_state.rag_engine)
        
        st.subheader("🔄 Generate Embeddings")
        render_embedding_generator(st.session_state.rag_engine)
        
        render_query_interface(st.session_state.rag_engine)
    
    with col2:
        render_status_info(st.session_state.rag_engine)
