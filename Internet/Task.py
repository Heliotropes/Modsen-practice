from selenium import webdriver

opt = webdriver.ChromeOptions()
WDriver = webdriver.Chrome(options=opt)
url = 'https://www.lightnovelworld.com/'

WDriver.get(url)

WDriver.execute_script("localStorage.setItem('SomeKey', 'AbraKaDabra');")

value = WDriver.execute_script("return localStorage.getItem('SomeKey');")
print(f"LocalStorage: {value}")

WDriver.execute_script("localStorage.removeItem('SomeKey');")

value = WDriver.execute_script("return localStorage.getItem('SomeKey');")
print(f"LocalStorage: {value}")

WDriver.get(url)

WDriver.add_cookie({"name": "SomeCookie", "value": "SomeValue"})

cookie = WDriver.get_cookie("SomeCookie")
print(f"Cookie: {cookie['value']}")

WDriver.delete_cookie("SomeCookie")

cookie = WDriver.get_cookie("SomeCookie")
print(f"Cookie: {cookie}")

WDriver.quit()
