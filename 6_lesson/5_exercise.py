from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запуск WebDriver в фоновом режиме
driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument("--headless"))
driver.get("https://parsinger.ru/selenium/6/6.3.2/index.html")
time.sleep(2)

# Удаляем все cookies
driver.delete_all_cookies()
time.sleep(2)

driver.refresh()  # Перезагружаем страницу, чтобы отобразился пароль

# Ждем появления пароля
try:
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text
    print(f"Пароль: {password}")
except:
    print("Пароль не найден")

driver.quit()