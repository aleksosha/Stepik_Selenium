from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://parsinger.ru/selenium/1/1.html")
    forms = browser.find_elements(By.CLASS_NAME, 'form')
    for form in forms:
        form.send_keys('Text')

    browser.find_element(By.ID, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    print(result)

finally:
    browser.quit()