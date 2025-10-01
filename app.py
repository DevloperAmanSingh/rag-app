import streamlit as st
from ui.rag import render_rag_analyzer


def main() -> int:
    try:
        render_rag_analyzer()
        return 0
    except Exception as exc:
        st.title("Simple RAG Analyzer")
        st.error("Failed to initialize RAG UI. Ensure 'llmware' is installed and configured.")
        st.exception(exc)
        return 1


if __name__ == "__main__":
    main()


