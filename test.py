from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver(chrome_path):
    chrome_options = Options()
    chrome_options.binary_location = chrome_path  # Chrome 실행 파일 경로
    chrome_options.add_argument("--headless=new")  # Headless 모드 (필요 시 제거 가능)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=chrome_options)

# Chrome 실행 파일 경로 (chrome.exe의 절대 경로)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 드라이버 설정
driver = setup_driver(chrome_path)

# 테스트: Google 페이지 열기
driver.get("https://www.miumiu.com/kr/ko/bags/c/10268KR")
# print(driver.title)  # 출력: "Google"

product_titles = driver.find_elements(By.CSS_SELECTOR, "h3.card__title")
print(product_titles)
# 작업 종료
driver.quit()
