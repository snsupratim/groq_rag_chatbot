import os
import logging
import warnings
import streamlit as st

from module.pdf_handler import upload_pdfs, load_pdfs
from module.vectorstore import load_vectorstore
from module.llm import get_llm_chain
from module.chat import display_chat_history, handle_user_input, download_chat_history
from module.chroma_inspector import inspect_chroma

# Suppress warnings and unnecessary logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

# Optional: Set your app title and favicon
st.set_page_config(page_title="Modular RAG Chatbot", page_icon="🤖")
st.title("🧠 Ask Your PDFs – RAG Chatbot")

# Upload PDF Files
uploaded_files = upload_pdfs()

# Submit button for processing PDFs
submitted = st.sidebar.button("📄 Submit PDFs for Processing")

if submitted and uploaded_files:
    with st.spinner("🔄 Updating vector database..."):
        documents = load_pdfs(uploaded_files)
        vectorstore = load_vectorstore(documents)
        st.session_state.vectorstore = vectorstore

if "vectorstore" in st.session_state:
    inspect_chroma(st.session_state.vectorstore)


# Display chat history
display_chat_history()

# Handle new queries if vectorstore is ready
if "vectorstore" in st.session_state:
    chain = get_llm_chain(st.session_state.vectorstore)
    handle_user_input(chain)

# Allow user to export chat history
download_chat_history()
