import requests
import json
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=2ePkmyjmWEOy1ym1qC6Dlba1dcJ8J2m9&data=AP01'
res = requests.get(url).text
data = json.loads(res)
print(type(data))
result = data[-1]['deal_bas_r']
# print(result,type(result))
print('='*40)
print(f'오늘의 환율은 1달러에 {result} 원입니다')
print('='*40)
