from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://parsinger.ru/selenium/3/3.3.2/index.html")
    blocks = browser.find_elements(By.CLASS_NAME, 'block')
    for block in blocks:
        block.find_element(By.CLASS_NAME, 'button').click()
    time.sleep(1)
    print(browser.find_element(By.TAG_NAME,'password').text)

finally:
    browser.quit()