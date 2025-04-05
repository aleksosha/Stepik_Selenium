from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')

try:
    browser.find_element(By.ID, 'showTextBtn').click()
    password = browser.find_element(By.ID, 'text1').text
    browser.find_element(By.ID, 'userInput').send_keys(password)
    browser.find_element(By.ID, 'checkBtn').click()
    code = browser.find_element(By.ID, 'text2').text
    print(code)
finally:
    browser.quit()
