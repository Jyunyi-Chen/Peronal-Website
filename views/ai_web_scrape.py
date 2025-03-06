import streamlit as st

from views.utils.parse import parse_with_gemini
from views.utils.scrape import scrape_website, extract_body_content, clean_body_content, split_content

st.title("AI Web Scraper (Powered by Gemini)")

url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website ...")

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

    parse_desc = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_desc:
            st.write("Parsing the content ...")

            # Parse the content with Ollama
            chunks: list[str] = split_content(st.session_state.content)
            parsed_result = parse_with_gemini(chunks, parse_desc)
            st.write(parsed_result)