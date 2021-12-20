import datetime
import time
# Импортируем селениум
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# подключаем драйвер
driver = webdriver.Chrome()

driver.get('https://www.labirint.ru/')

# Тест - кейс №1 - тестирование работоспособности  поисковой строки
search_box = driver.find_element(By.XPATH,
                                 '//*[@id="search-field"]')
search_box.send_keys('мойдодыр')
time.sleep(1)
search_button = driver.find_element(By.XPATH,
                                 '//*[@id="searchform"]/div[1]/button/span[1]')
search_button.click()

answer = driver.find_element(By.XPATH,
                             '//*[@id="catalog-navigation"]/form/div[3]/div[2]/input')

if answer.text != u'мойдодыр':
    print(datetime.datetime.now(), "№1 Ожидаемый ответ верен =  мойдодыр", answer.text)
else:
    print("Ожидаемый ответ ", answer.text, " не найден")

time.sleep(2)
#driver.quit()
#Тест - кейс № 2 Проверка фильтрации товаров
search_button2 = driver.find_element(By.XPATH,
                                 '//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[5]/span/span/span/span')
search_button2.click()
time.sleep(1)
search_button3 = driver.find_element(By.XPATH,
                                 '//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
search_button3.click()
time.sleep(1)
search_button4 = driver.find_element(By.XPATH,
                                 '//*[@id="section-search-form"]/div[1]/div[2]/div[1]/label')
search_button4.click()
time.sleep(2)
search_button5 = driver.find_element(By.XPATH,
                                 '//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]')
search_button5.click()
print(datetime.datetime.now(), '№2 Фильтрация товаров прошла успешно')
time.sleep(4)
#Тест-кейс №3 проверка кликабельности кнопки "Добавить товар в отложенное - (сердечко)  "
search_button6 = driver.find_element(By.XPATH,
                                 '//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/div/div[1]/div/div[4]/div/div[2]/div/div/a[1]/span')
search_button6.click()
print(datetime.datetime.now(), '№3 товар успешно добавлен в отложенное  ')
#Тест-кейс №4 проверка кликабельности кнопки - перейти в отложенные товары во всплывающем окне добавленного раннее товара
time.sleep(4)
search_button7 = driver.find_element(By.XPATH,
                                 '//*[@id="minwidth"]/div[2]/div/div[1]/div/div/a')
search_button7.click()
time.sleep(5)
search_button8 = driver.find_element(By.XPATH,
                                 '//*[@id="buyingbtns808437"]/div[1]/a[1]/span')
search_button8.click()


print(datetime.datetime.now(), '№4 Успешно осуществлен переход в отложенные товары  ')
# Тест-кейс № 5 Добавление товара в корзину из раздела "Отложенные"
time.sleep(3)
search_button9 = driver.find_element(By.XPATH,
                                 '//*[@id="buy808437"]')
search_button9.click()
print(datetime.datetime.now(), '№5 Добавление товара в корзину выполнено  ')
# Тест-кейс №6 Оформление заказа
time.sleep(4)
search_button10 = driver.find_element(By.XPATH,
                                 '//*[@id="minwidth"]/div[2]/div/div[1]/div/a')
search_button10.click()
print(datetime.datetime.now(), '№6 Переход во вкладку "Оформление товара" осуществлен  ')
time.sleep(4)
driver.quit()









