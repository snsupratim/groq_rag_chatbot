import streamlit as st

def display_chat_history():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

def handle_user_input(chain):
    prompt = st.chat_input("Ask your question...")
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        result = chain({"query": prompt})
        response = result["result"]

        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({'role': 'assistant', 'content': response})

def download_chat_history():
    with st.sidebar:
        if st.download_button("📥 Download Chat History", data="\n\n".join([
            f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.get("messages", [])
        ]), file_name="chat_history.txt"):
            st.success("Chat history downloaded!")




