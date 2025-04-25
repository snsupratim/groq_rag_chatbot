import streamlit as st
from langchain.document_loaders import PyPDFLoader

def upload_pdfs():
    with st.sidebar:
        uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    return uploaded_files

def load_pdfs(uploaded_files):
    docs = []
    for file in uploaded_files:
        with open(f"temp_{file.name}", "wb") as f:
            f.write(file.read())
        loader = PyPDFLoader(f"temp_{file.name}")
        docs.extend(loader.load())
    return docs