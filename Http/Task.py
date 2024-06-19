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