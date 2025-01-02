import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import pandas as pd

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


def parse_html(html_content, base_url):
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

            # 상품 링크 (상대 경로 -> 절대 경로 변환)
            relative_link = card.find("a", href=True)["href"]
            product_url = urljoin(base_url, relative_link)

            # 가격 추출
            # srcset 속성에서 첫 번째 URL 추출
            # 이미지 태그 찾기
            image_tag = card.find("source").get("data-srcset")
            image_url = image_tag.split(",")[0].strip()

            product_data.append({
                "상품명": title,
                "가격": price,
                "상품 링크 URL": product_url,
                "이미지 URL":image_url
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

def save_to_excel(data, filename="output.xlsx"):
    """
    Saves the data to an Excel file.
    """
    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # 데이터가 비어 있는지 확인
    if df.empty:
        print("No data to save.")
        return

    # 엑셀 파일 저장
    try:
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error while saving to Excel: {e}")
