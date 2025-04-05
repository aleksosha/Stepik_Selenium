import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/7/7.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.CLASS_NAME, 'content').click()
    fields = browser.find_elements(By.TAG_NAME, 'option')
    total_sum = 0
    for field in fields:
        number = int(field.text)
        total_sum += number
    browser.find_element(By.ID, 'input_result').send_keys(total_sum)
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)

