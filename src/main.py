import json
import re
import urllib3.request

url = "https://store.playstation.com/valkyrie-api/ru/RU/999/container/STORE-MSF75508-FULLGAMES?sort=release_date&direction=desc&size=100&bucket=games&start=0"
http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.status)

json_string = r.data
data = json.loads(json_string)

full_list = data['included']
game_titles = list()
exclude_keywords = ['Цифровое', 'Digital', 'Предзаказ', 'Pre-Order', 'Pre Order', 'предварительный', 'цифрового']

for i in range(len(full_list)):
    element = full_list[i]
    element_type = full_list[i]['type']

    if element_type == 'game' and element['attributes']['skus'][0]['is-preorder'] == False:
        game_name = element['attributes']['name']

        print(i, game_name)
