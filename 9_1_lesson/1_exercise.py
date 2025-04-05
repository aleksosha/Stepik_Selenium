import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/9/9.1.1/index.html")
    for button in browser.find_elements(By.XPATH, '//button'):
        # передаем кнопку в функцию element_to_be_clickable (button)
        WebDriverWait(browser, 12).until(EC.element_to_be_clickable(button)).click()
    print(browser.find_element(By.ID, 'message').text)