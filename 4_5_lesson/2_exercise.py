from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://parsinger.ru/selenium/3/3.3.1/index.html")
    child = browser.find_element(By.ID, 'parent_id').find_element(By.CLASS_NAME,'child_class' )
    child.click()
    print(child.get_attribute('password'))
finally:
    browser.quit()