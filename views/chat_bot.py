import os
import time
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

        full_response = ""
        for char in response:
            full_response += char
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.005)
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})