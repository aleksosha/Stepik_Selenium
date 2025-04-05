from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")
    browser.find_element(By.ID, "clickButton").click()
    time.sleep(5)
finally:
    browser.quit()