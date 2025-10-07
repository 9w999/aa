# APIリクエストに必要なライブラリ
import requests
# URL＋クエリパラメータ
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=400040'
# APIリクエストを送信
tenki_data = requests.get(url).json()
print(tenki_data)
