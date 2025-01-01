import requests
from bs4 import BeautifulSoup
import os

def fetch_html(url):
    """
    Fetches HTML content from the URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # HTTP 에러 발생 시 예외 처리
    return response.text


def parse_html(html_content):
    """
    Parses HTML content and extracts relevant data.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # 필요한 데이터 추출 (예: 상품명과 가격)
    product_data = []
    product_cards = soup.find_all("article", class_="card")

    for card in product_cards:
        try:
            # 상품명 추출
            title = card.find("h3", class_="card__title").get_text(strip=True)

            # 가격 추출
            price = card.find("p", class_="card__price").get_text(strip=True)

            # 링크 추출
            link = card.find("a", href=True)["href"]
            product_data.append({
                "Product Name": title,
                "Price": price,
                "Link": f"https://www.miumiu.com{link}"
            })
        except AttributeError:
            # 일부 데이터가 없는 경우 예외 처리
            continue

    return product_data


def save_html(html_content, filename="output.html"):
    """
    Saves raw HTML content to a file for debugging.
    """
    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", filename)
    with open(path, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"HTML saved to {path}")
