import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

template = (
    "You are tasked with extracting specific information from the following text content: {content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_desc}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_gemini(chunks, parse_desc):
    parsed_results = []
    for i, chunk in enumerate(chunks, start=1):
        prompt_text = template.format(content=chunk, parse_desc=parse_desc)
        response = gemini_model.generate_content(prompt_text)
        parsed_text = response.text.strip() if response.text else ""
        print(f"Parsed batch: {i} of {len(chunks)}")
        parsed_results.append(parsed_text)
    return "\n".join(parsed_results)
