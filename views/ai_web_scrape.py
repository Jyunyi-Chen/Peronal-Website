import streamlit as st

from views.utils.parse import parse_with_gemini
from views.utils.scrape import scrape_website, extract_body_content, clean_body_content, split_content

col1, col2 = st.columns([3, 1])

with col1:
    st.title("AI Web Scraper", anchor=False)

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

url = st.text_input(label="", placeholder="Enter Website URL ...")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write(f"🔎 Scraping the website ...")

        # Scrape the website
        html: str = scrape_website(url)
        body: str = extract_body_content(html)
        content: str = clean_body_content(body)

        # Store the content in Streamlit session state
        st.session_state.content = content

# Step 2: Ask Questions About the Content
if st.session_state.get("content"):
    
    with st.expander("View Content", expanded=True):
        st.text_area("Content", st.session_state["content"], height=300)

    parse_desc = st.text_input(label="", placeholder="Describe what you want to parse ...")

    if st.button("Parse Content"):
        if parse_desc:
            st.write(f"🤖 Parsing the content with {selected_display_name} ...")

            chunks: list[str] = split_content(st.session_state.content)
            parsed_result = parse_with_gemini(chunks, parse_desc, selected_model)
            st.write(parsed_result)
