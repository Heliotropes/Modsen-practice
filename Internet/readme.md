### Internet
--- 
#### Задание:
Необходимо использовать библиотеку Selenium для работы, которая позволяет 
автоматизировать веб-браузеры и взаимодействовать с веб-элементами. Для начала
установите библиотеку Selenium, также Вам потребуется веб-драйвер для вашего браузера 
(например, ChromeDriver для Google Chrome).


#### Средства реализации:

Среда разработки: _Python 3.12.2_
Инструмент для взаимодействия с веб-элементами: модуль _Selenium_

#### Реализация:
Код скрипта:

    from selenium import webdriver

    opt = webdriver.ChromeOptions()
    WDriver = webdriver.Chrome(options=opt)
    url = 'https://www.lightnovelworld.com/'

    WDriver.get(url)

    WDriver.execute_script("localStorage.setItem    ('SomeKey', 'AbraKaDabra');")

    value = WDriver.execute_script("return localStorage.    getItem('SomeKey');")
    print(f"Значение из LocalStorage: {value}")

    WDriver.execute_script("localStorage.removeItem ('SomeKey');")

    value = WDriver.execute_script("return localStorage.    getItem('SomeKey');")
    print(f"Значение после удаления: {value}")

    WDriver.get(url)

    WDriver.add_cookie({"name": "SomeCookie", "value":  "SomeValue"})

    cookie = WDriver.get_cookie("SomeCookie")
    print(f"Значение cookie: {cookie['value']}")

    WDriver.delete_cookie("SomeCookie")

    cookie = WDriver.get_cookie("SomeCookie")
    print(f"Cookie после удаления: {cookie}")

    WDriver.quit()

Результат:

    DevTools listening on ws://127.0.0.1:60365/devtools/browser/82a2a8e8-8c82-4db7-a945-937cc45a3c5e
    LocalStorage: AbraKaDabra
    LocalStorage: None
    Cookie: SomeValue
    Cookie: None

