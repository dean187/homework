import requests

paramDict = {"a": "bbb", "b": 123}
url = "http://www.naver.com"
response = requests.get(url, params=paramDict)
print("status code :", response.status_code)​
