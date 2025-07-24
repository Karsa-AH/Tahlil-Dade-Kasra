from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from io import BytesIO
import requests, time, os

def scrape_and_download():
    driver = webdriver.Chrome(service=Service(r"C:\Users\Asus\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"))
    driver.get("https://divar.ir/s/tehran/auto?q=206")
    time.sleep(3)
    os.makedirs("images", exist_ok=True)

    for _ in range(200):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        try:
            btn = driver.find_element(By.CLASS_NAME, "post-list__load-more-btn-be092")
            if btn.is_displayed():
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)
        except NoSuchElementException:
            pass

    cards = driver.find_elements(By.CLASS_NAME, "widget-col-d2306")

    for card in cards:
        try:
            title = card.find_element(By.CLASS_NAME, "kt-post-card__title").text
            if "206" not in title and "۲۰۶" not in title:
                continue

            img = card.find_element(By.CLASS_NAME, "kt-image-block__image--lazy-loaded")
            src = img.get_attribute("src")
            if not src or not src.startswith("http"):
                continue

            try:
                res = requests.get(src, timeout=5)
                image = Image.open(BytesIO(res.content))
                filename = f"car_{len(os.listdir('images'))+1}.{image.format.lower()}"
                image.save(os.path.join("images", filename))
            except:
                pass

        except:
            pass

    driver.quit()

scrape_and_download()
