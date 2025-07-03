from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

webdriver_path = Path(__file__).resolve().parent/"chromedriver"

topic_user_input = input("Enter topic to search\n>>")

service = Service(executable_path = str(webdriver_path))
driver = webdriver.Chrome(service = service)

driver.get("https://www.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys(topic_user_input, Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mw-content-text"))
)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

for sup in soup.find_all("sup", class_= "reference"):
    sup.decompose()

intro_div_children = soup.find(id = "mw-content-text").find(class_ = "mw-parser-output").children

with open("notes.md", "w+") as f:
    pass

with open("notes.md", "a+") as f:
    for element in intro_div_children:
        if not hasattr(element, "get"):
            continue
        if "mw-heading" in element.get("class", []) :
            break
        if element.name == "p":
            f.write(element.text.strip())

driver.quit()
