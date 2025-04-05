from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    browser.find_element(By.ID, 'secret-key-button').click()
    button = browser.find_element(By.ID, 'secret-key-button').get_attribute('data')
    print(button)

finally:
    browser.quit()