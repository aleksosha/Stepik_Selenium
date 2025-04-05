import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
    height = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script(f"window.scrollTo(0, {height});")

    time.sleep(2)  # Ждем появления пароля

    # Извлекаем пароль
    password_element = browser.find_element(By.ID, "secret-container")
    password = password_element.text
    print(password)