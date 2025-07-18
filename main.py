from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def user_input():
    global user_search_query
    user_search_query = input("Enter topic to search\n>>")

def connect_to_wikipedia():
    try:
        driver.get("https://www.wikipedia.org/")
    except selenium.common.exceptions.WebDriverException:
        print("check your internet connection")

def search_for_wiki():
    global search_box
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys(user_search_query, Keys.ENTER)

def remove_citations():
    for sup in soup.find_all("sup", class_= "reference"):
        sup.decompose()

def wait(time, condition):
    WebDriverWait(driver, time).until(condition)

def navigate_to_elements():
    try:
        global elements
        elements = soup.find(id = "mw-content-text").find(class_ = "mw-parser-output").children
    except AttributeError:
        print("Page Not Found")

def save_to_file():
    with open("notes.md", "w+") as f:
        pass

    with open("notes.md", "a+") as f:
        for element in elements:
            if not hasattr(element, "get"):
                continue
            if "mw-heading" in element.get("class", []) :
                break
            if element.name == "p":
                f.write(element.text.strip())


webdriver_path = Path(__file__).resolve().parent/"chromedriver"

service = Service(executable_path = str(webdriver_path))
driver = webdriver.Chrome(service = service)

user_input()
connect_to_wikipedia()
search_for_wiki()
wait(10, EC.presence_of_element_located((By.ID , "mw-content-text")))

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

remove_citations()
navigate_to_elements()
save_to_file()

driver.quit()
