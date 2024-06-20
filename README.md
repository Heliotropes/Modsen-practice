### 1. HTTP
--- 
#### Задание:
Необходимо получить все статусы ответов на HTTP-запрос.

#### Средства реализации:

Среда разработки: _Python 3.12.2_
Инструмент для использования протокола HTTP: модуль _Requests_

#### Реализация:
Код скрипта:

    import requests
    
    appid = 'e4bb0753974e1cf770eb715bb642bda4'
    url2 = f"https://api.openweathermap.org/data/2.5/weather?lat=53.9&lon=27.57&appid={appid}"
    url3 = f"https://www.mediawiki.com/w/api.php"
    url4 = f"https://api.openweathermap.org/data/2.5/weather?lat=&lon=27.57&appid={appid}"
    
    payload = {}
    headers = {}
    
    response2 = requests.request("GET", url2, headers=headers, data=payload)
    response3 = requests.request("GET", url3,allow_redirects=False, headers=headers, data=payload)
    response4 = requests.request("GET", url4, headers=headers, data=payload)
    
    print(response2.status_code, response3.status_code,response4.status_code)

Результат:

    200 301 400

#### О деталях реализации и полученном результате:

Было отправлено три HTTP-запроса. На первый запрос был получен ответ, чей код статуса равен 200. То есть он принадлежит к группе "Успешные ответы", и сам код означает, что запрос успешно выполнен. В данном случае мы получим ответ с метеорологическими данными по месту, координаты которого написаны в URL.

Во втором случае был получен ответ из группы "Сообщения о перенаправлении". А сам код 301 означает, что URL-адрес запрошенного ресурса был изменен навсегда и новый URL-адрес указан в ответе.
    
    www.mediawiki.com -> www.mediawiki.org

Для того, чтобы была возможность получить код ответа 3xx, важно изменить один аргумент в запросе:

    allow_redirects=False

В модуле _Requests_ он по умолчанию имеет значение _True_, из-за чего в случае перенаправления он автоматический перейдёт на новый URL-адрес и вернёт ответ c кодом 2xx, если запрос был успешный.

В третьем случае был получен статус ответа 400. Данная группа ответов сообщает об "Ошибке клиента". Номер 400 означает, сервер не может или не будет обрабатывать запрос из-за чего-то, что воспринимается как ошибка клиента, в данном случае это ошибка в синтакисе URL-адреса, а именно пропущено значение одного из параметров, географической широты.

Что касается ответов группы 1xx и 5xx.

Оветы первой группы относятся к "Информационным ответам". Поскольку эти ответы указывают только на информационный статус запроса, они являются промежуточными, а не финальными. Рассмотрим ответ с кодом 100. Он означает, что клиент должен продолжить запрос или игнорировать его, если он уже завершён. То есть сначала требуется отправить заголовки запроса, одним из которых будет: 

    Expect: 100-continue

После чего можно получить промежуточный ответ от сервера с кодом 100, если запрос был принят. После чего происходит отправка тела запроса на сервер.

Однако в данном случае ответ с кодом 100 не может быть получен, поскольку модуль _Requests_ игнорирует заголовок _Expect_.

Ответы пятой группы означают "Ошибки сервера". Это может быть какая-либо неисправность, ошибка, недочёт, несоответствие со стороны сервера. Поскольку в данном случае я выступаю только со стороны клиента эта группа кодов ответов не была получена. Хотя даже, действуя со стороны клиента, можно получить ответ группы 5xx. Наиболее подходящими будут ошибки 501 и 505. Первая говорит об отсутвии поддержки метода запроса, а вторая об отсутвии поддержки версии HTTP-запроса.
