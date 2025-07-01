from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

webdriver_path = Path(__file__).resolve().parent/"chromedriver"

topic_user_input = input("Enter topic to search\n>>")

service = Service(executable_path = str(webdriver_path))
driver = webdriver.Chrome(service = service)

driver.get("https://www.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys(topic_user_input, Keys.ENTER)

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#mw-content-text .mw-parser-output > *"))
)
elements = driver.find_elements(By.CSS_SELECTOR,"#mw-content-text .mw-parser-output > *")

for element in elements:
    if element.get_attribute("class") == "mw-heading mw-heading2":
        break
    elif element.tag_name == "p":
        print(element.text.strip())

time.sleep(10)

driver.quit()
