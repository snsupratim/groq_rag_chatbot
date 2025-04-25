from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
embedding_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2')

def load_vectorstore(documents):
    texts = text_splitter.split_documents(documents)
    vectorstore = Chroma.from_documents(documents=texts, embedding=embedding_model)
    return vectorstore