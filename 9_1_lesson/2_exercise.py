import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/9/9.2.1/index.html")

    browser.find_element(By.ID, 'startScan').click()
    WebDriverWait(browser, 20).until(EC.title_is("Access Granted"))
    print(browser.find_element(By.CLASS_NAME, 'highlight').text)