from selenium import webdriver
from selenium.webdriver.common.by import By

# Указываем путь к драйверу (например, для Chrome)
driver = webdriver.Chrome()

# Шаг 1: Открываем сайт
driver.get("https://parsinger.ru/selenium/6/6.3.3/index.html")

# Шаг 2: Устанавливаем cookie
cookie = {"name": "secretKey", "value": "selenium123"}
driver.add_cookie(cookie)

# Шаг 3: Обновляем страницу
driver.refresh()

# Шаг 4: Извлекаем пароль
password_element = driver.find_element(By.ID, "password")
password = password_element.text

# Шаг 5: Выводим пароль
print(f"Пароль: {password}")

# Закрываем браузер
driver.quit()
