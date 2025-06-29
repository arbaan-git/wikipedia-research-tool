from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = Path(__file__).resolve().parent/"chromedriver"

topic_user_input = input("Enter topic to search\n>>")

service = Service(executable_path = str(webdriver_path))
driver = webdriver.Chrome(service = service)

driver.get("https://www.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys(topic_user_input, Keys.ENTER)


time.sleep(10)

driver.exit()
