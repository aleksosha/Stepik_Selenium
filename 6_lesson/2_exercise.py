from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.2.1/index.html")

    browser.find_element(By.ID, 'this_pic').screenshot('2_exercise_screenshot.png')
