from selenium import webdriver # импортируем драйвер
from selenium.webdriver.common.by import By

driver=webdriver.Chrome() # создаем объект драйвера класса Chrome
driver.get= "https://demoqa.com/"  # вызываем метод get и передаем в него url, должна открыться страница
# модуль для поиска элемента веб-страницы
icon=driver.find_element(By.CSS_SELECTOR, "header > a > img")
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
