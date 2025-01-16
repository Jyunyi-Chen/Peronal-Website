import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Chatbot (Powered by Gemini)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("Enter your question ..."):
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = model.generate_content(query).text
        message_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})