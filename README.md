# -4--Selenium

С помощью фрейворк Seleniun автоматизируйте 6 тест-кейсов  из  задания №1

Для создания приложения автоматического тестирования сайта был выбран сайт лабиринт https://www.labirint.ru/ , который использовался при ручном тестировании в первом задании. 

Описание проделанной работы: С помощью модуля pip устанавливаем selenium: pip install selenium  Selenium предоставляет следующие методы поиска элементов на странице:

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

Для удобства, в работе активно используется метод find_element_by_xpath - для поиска определенного элемента по его id. Также используется метод click - проверка работы сайта при нажатии на кнопку. Было выбрано 6 тест-кейсов из ручного тестирования: Поиск в поисковой строке, выбор товара, фильтрация товаров, добавление товаров в отложенное и в корзину, нажатие кнопки - "Начать оформление". В качестве подтверждения корректной работы программы приложен скрин с выполненными тестами и скрины пошаговых изображений всех действий на сайте. Стоит отметить, что для работы с элементами через Xpath - была подключена библиотека  selenium.webdriver.common.by, Xpath — это язык запросов к элементам xml или xhtml. документа. 

Скрины проделанной работы : 
- скрин написания функции для введения текста в поисковую строку

![image](https://user-images.githubusercontent.com/92279258/146774786-faa9e3d4-2352-4dfa-992b-d32783f872b5.png)

Далее - скрины пошаговыхотображений всех действий на сайте 

![image](https://user-images.githubusercontent.com/92279258/146774908-8b821d71-1fe6-4886-a30a-2c1924283b55.png)

![image](https://user-images.githubusercontent.com/92279258/146774948-fb8aa87c-bef9-438a-9d48-22c0bbb26548.png)

![image](https://user-images.githubusercontent.com/92279258/146774978-bd2060e4-ed85-4cee-a933-034040a0df7d.png)

![image](https://user-images.githubusercontent.com/92279258/146775310-21199b48-7adb-4236-9213-3e22fc0080ea.png)

![image](https://user-images.githubusercontent.com/92279258/146775354-1c06f95c-6cc9-4bf5-a3dd-5fce347480fe.png)

![image](https://user-images.githubusercontent.com/92279258/146775380-7ab62dd8-6daf-4c26-bedf-edec0f3cbcd3.png)

![image](https://user-images.githubusercontent.com/92279258/146775406-5e8a3eb1-a991-4833-b05b-68c1c1b76626.png)

![image](https://user-images.githubusercontent.com/92279258/146775437-38e89d7f-8e35-4815-b5fc-b6af21dc678a.png)

![image](https://user-images.githubusercontent.com/92279258/146775451-c3cf2447-0f73-4587-923c-b09107a35c52.png)

-Скрин - подтверждение, что все тест-кейсы выполнены 

![image](https://user-images.githubusercontent.com/92279258/146775584-e2b5b67a-cad7-4f30-9127-35af9870cd0c.png)


