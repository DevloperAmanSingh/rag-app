import streamlit as st
from models.rag_engine import RAGEngine


def render_document_loader(rag_engine: RAGEngine) -> None:
    
    source_choice = st.radio(
        "Document source",
        ("Use LLMWare sample invoices (may download)", "Use local folder", "Upload files"),
        index=0,
    )

    if source_choice == "Upload files":
        uploaded_files = st.file_uploader(
            "Upload invoice documents", 
            accept_multiple_files=True, 
            type=['pdf', 'txt', 'docx']
        )
        if uploaded_files and st.button("Process Uploaded Files"):
            with st.spinner("Processing uploaded files..."):
                success = rag_engine.create_library_from_uploads(uploaded_files)
                if success:
                    st.success(f"Processed {len(uploaded_files)} files")
                else:
                    st.error("Failed to process uploaded files")
    
    elif source_choice == "Use local folder":
        local_path = st.text_input("Local folder with invoices (PDFs)", value="")
        if local_path and st.button("Load Local Files"):
            with st.spinner("Loading local files..."):
                success = rag_engine.create_library_from_folder(local_path)
                if success:
                    st.success("Local files loaded")
                else:
                    st.error("Failed to load local files")
    
    else:
        if st.button("Load Sample Invoices"):
            with st.spinner("Preparing sample invoices (first run can take a minute)..."):
                success = rag_engine.create_library_from_samples()
                if success:
                    st.success("Sample invoices loaded")
                else:
                    st.error("Failed to load sample invoices")


def render_embedding_generator(rag_engine: RAGEngine) -> None:
    status = rag_engine.get_library_status()
    
    if status["has_library"] and not status["embeddings_ready"]:
        if st.button("Generate Embeddings"):
            with st.spinner("Generating embeddings (this may take a few minutes)..."):
                success = rag_engine.generate_embeddings()
                if success:
                    st.success("Embeddings generated successfully!")
                else:
                    st.error("Failed to generate embeddings")
    
    elif status["has_library"] and status["embeddings_ready"]:
        st.success("✅ Embeddings are ready!")
    
    elif not status["has_library"]:
        st.info("Please load documents first.")
