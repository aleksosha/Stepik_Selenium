from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск WebDriver в фоновом режиме
driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument("--headless"))
driver.get("https://parsinger.ru/selenium/6/6.3/index.html")
time.sleep(2)

# Получаем cookies и ищем название песни
cookies = {cookie["name"].lower(): cookie["name"] for cookie in driver.get_cookies()}
song_name = cookies.get("who let the dogs out")

if song_name:
    print(f"Найдено название песни: {song_name}")
    driver.find_element(By.ID, "phraseInput").send_keys(song_name)
    driver.find_element(By.ID, "checkButton").click()
    time.sleep(2)
    print(f"Девиз: {driver.find_element(By.ID, 'result').text}")
else:
    print("Название песни не найдено в cookies")

driver.quit()