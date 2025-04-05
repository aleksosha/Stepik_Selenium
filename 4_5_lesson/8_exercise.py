from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/4/4.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    boxes = browser.find_elements(By.CLASS_NAME, 'check')
    for box in boxes:
        box.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)