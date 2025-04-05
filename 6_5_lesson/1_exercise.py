from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем браузер без дополнительных опций
driver = webdriver.Chrome()

# 1️⃣ Открываем сайт
driver.get("https://parsinger.ru/selenium/6/6.5/index.html")

# 2️⃣ Находим кнопку и прокручиваем к ней через JavaScript
button = driver.find_element(By.ID, "target")
driver.execute_script("arguments[0].scrollIntoView();", button)

# 3️⃣ Кликаем по кнопке "Финиш!"
button.click()

# 4️⃣ Делаем паузу на всякий случай
time.sleep(1)

# 5️⃣ Извлекаем текст с ключом
secret_text = driver.find_element(By.ID, "secret-key").text

# 6️⃣ Оставляем только сам ключ, без "Ваш ключ:"
secret_key = secret_text.split(":")[1].strip()

# 7️⃣ Выводим результат
print(f'"{secret_key}"')

# Закрываем браузер
time.sleep(2)
driver.quit()
