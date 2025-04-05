from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    browser.find_element(By.ID, 'codeInput').send_keys('Дрогон')
    browser.find_element(By.ID, 'clickButton').click()
    time.sleep(5)
finally:
    browser.quit()
