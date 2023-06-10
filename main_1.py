import json
import requests

url = 'https://search-maps.yandex.ru/v1/'
city = 'Новокузнецк'
key = 'стоматология'
keyword = city + ', ' + key

params = {
    'apikey': '658f4f45-eafa-435c-abdc-dccb52a2556b',
    'text': keyword,
    'lang': 'ru_RU',
    'results': 500
}

r = requests.get(url, params=params)

with open('cities/Novokuznetsk/save.json', 'w', encoding='utf8') as f:
    f.write(r.text)
