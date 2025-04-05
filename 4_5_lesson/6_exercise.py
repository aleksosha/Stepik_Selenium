from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    blocks = browser.find_elements(By.TAG_NAME, 'p')

    total_sum = 0
    for block in blocks:
        number = int(block.text)
        total_sum += number
    print(total_sum)
