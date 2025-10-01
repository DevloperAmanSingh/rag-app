import streamlit as st
from models.rag_engine import RAGEngine


def render_query_interface(rag_engine: RAGEngine) -> None:
    status = rag_engine.get_library_status()
    
    if not status["has_library"]:
        st.info("Please load documents first.")
        return
    
    if not status["embeddings_ready"]:
        st.info("Please generate embeddings to enable document search.")
        return
    
    st.subheader("Ask Questions")
    
    prompt_text = st.text_area(
        "Ask a question about your documents",
        placeholder="Example: What is the total amount of the invoice?",
    )

    if st.button("Search and Answer"):
        if not prompt_text:
            st.error("Please enter a question.")
            return

        with st.spinner("Searching documents and generating answer..."):
            result = rag_engine.query_documents(prompt_text)
            
            if "error" in result:
                st.error(f"Error: {result['error']}")
                return
            
            if result["success"] and result["response"]:
                response = result["response"]
                if isinstance(response, list) and "llm_response" in response[0]:
                    st.subheader("Answer")
                    st.write(response[0]["llm_response"])
                    
                    query_results = result.get("query_results", [])
                    if query_results:
                        st.subheader("Source Documents")
                        for i, result_item in enumerate(query_results[:3]):
                            text = result_item.get('text', '')
                            if text:
                                st.write(f"**Source {i+1}:** {text[:200]}...")
            else:
                st.warning("No response generated. Please try a different question.")


def render_status_info(rag_engine: RAGEngine) -> None:
    status = rag_engine.get_library_status()
    
    with st.sidebar:
        st.subheader("Status")
        if status["has_library"]:
            st.success("✅ Documents loaded")
        else:
            st.info("📁 No documents loaded")
            
        if status["embeddings_ready"]:
            st.success("✅ Embeddings ready")
        else:
            st.info("🔄 Embeddings not ready")
