import streamlit as st

def inspect_chroma(vectorstore):
    with st.sidebar:
        st.markdown("### 🔍 Inspect Chunks by Query")
        query = st.text_input("Enter a query to retrieve relevant chunks", key="inspect_query")

        if query:
            try:
                docs = vectorstore.similarity_search(query, k=3)
                if docs:
                    for i, doc in enumerate(docs):
                        st.markdown(f"**Chunk {i+1}:** {doc.page_content[:300]}...")
                else:
                    st.warning("No relevant chunks found.")
            except Exception as e:
                st.error(f"Error inspecting vector store: {e}")
