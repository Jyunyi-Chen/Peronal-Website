import os
import time
import streamlit as st
import google.generativeai as genai

col1, col2 = st.columns([3, 1])

with col1:
    st.title("AI Chat Bot", anchor=False)

model_options = {
    "Gemini 2.0 Flash": "gemini-2.0-flash",
    "Gemini 2.0 Flash-Lite": "gemini-2.0-flash-lite",
    "Gemini 1.5 Flash": "gemini-1.5-flash",
    "Gemini 1.5 Flash-8B": "gemini-1.5-flash-8b",
    "Gemini 1.5 Pro": "gemini-1.5-pro"
}
display_names = list(model_options.keys())

with col2:
    selected_display_name = st.selectbox(label="", options=display_names, index=2)

selected_model = model_options[selected_display_name]

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model = genai.GenerativeModel(selected_model)

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

        response_obj = model.generate_content(query)

        if response_obj.parts:
            response = "".join([part.text for part in response_obj.parts])
        else:
            response = (
                "⚠️ Response blocked: The model detected potentially copyrighted content "
                "and did not return any output. Please try rephrasing your prompt."
            )

        full_response = ""
        for char in response:
            full_response += char
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.005)
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})
