from selenium import webdriver

# Запуск браузера
driver = webdriver.Chrome()

# Открытие сайта
driver.get("https://parsinger.ru/selenium/6/6.3.1/index.html")

# Получение всех cookies
cookies = driver.get_cookies()

# Поиск нужного cookie
token_value = None
for cookie in cookies:
    if cookie["name"] == "token_22":
        token_value = cookie["value"]
        break

# Вывод значения cookie
print(token_value)

# Завершение работы с браузером
driver.quit()
