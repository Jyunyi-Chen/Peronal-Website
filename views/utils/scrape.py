import requests

from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    print("Fetching website content ...")
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return ""

def extract_body_content(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    if body:
        return str(body)
    return ""

def clean_body_content(body: str) -> str:
    soup = BeautifulSoup(body, "html.parser")
    for content in soup(["script", "style"]):
        content.extract()
    cleaned_body = soup.get_text(separator="\n")
    cleaned_body = "\n".join(
        [line.strip() for line in cleaned_body.splitlines() if line.strip()])
    return cleaned_body

def split_content(content: str, max_length: int = 6000):
    return [content[i:i + max_length] for i in range(0, len(content), max_length)]
