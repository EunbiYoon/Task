from crawler import fetch_html, parse_html, save_html

if __name__ == "__main__":
    url = "https://www.miumiu.com/kr/ko/bags/c/10268KR"

    try:
        # HTML 데이터 가져오기
        print("Fetching HTML content...")
        html_content = fetch_html(url)

        # HTML 파일 저장 (디버깅용)
        save_html(html_content)

        # HTML 데이터 파싱
        print("Parsing HTML content...")
        product_data = parse_html(html_content)

        # 결과 출력
        if product_data:
            for idx, product in enumerate(product_data, start=1):
                print(f"{idx}. {product['Product Name']} - {product['Price']} - {product['Link']}")
        else:
            print("No products found.")

    except Exception as e:
        print(f"An error occurred: {e}")
