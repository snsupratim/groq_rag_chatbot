import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

from langchain_core.prompts import ChatPromptTemplate

def get_llm_chain(vectorstore):
    model = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name="llama3-8b-8192"
    )

    chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type='stuff',
        retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
        return_source_documents=True
    )
    return chain