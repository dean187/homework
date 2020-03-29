import requests  # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
result = r.json()

mise_info = result['RealtimeCityAir']['row']
for mise in mise_info:
    gu_name = mise['MSRSTE_NM']
    gu_mise = mise['IDEX_MVL']
    print(gu_name, gu_mise)

for gu in mise_info:
    if gu['IDEX_MVL'] > 80:
        print(gu['MSRSTE_NM'], gu['IDEX_MVL'])