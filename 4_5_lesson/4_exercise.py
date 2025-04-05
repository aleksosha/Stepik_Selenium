from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)

    links = browser.find_elements(By.TAG_NAME, 'a')

    stormtrooper_count = 0
    for link in links:
        stormtrooper_value = link.get_attribute("stormtrooper")
        if stormtrooper_value and stormtrooper_value.isdigit():
            stormtrooper_count += int(stormtrooper_value)  # Исправлено

    input_field = browser.find_element(By.ID, "inputNumber")
    input_field.send_keys(str(stormtrooper_count))

    check_button = browser.find_element(By.ID, "checkBtn")
    check_button.click()

    password = browser.find_element(By.ID, "feedbackMessage").text
    print(password)

    browser.quit()
