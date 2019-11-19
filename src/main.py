import json
import re
import urllib3.request

url = "https://store.playstation.com/valkyrie-api/ru/RU/999/container/STORE-MSF75508-FULLGAMES?sort=release_date&direction=desc&size=200&bucket=games&start=0"
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

    if element_type == 'game':
        game_name = element['attributes']['name']
        skip = False
        for j in range(len(exclude_keywords)):
            if re.search(exclude_keywords[j-1], game_name):
                skip = True
        if not skip:
            game_titles.append(game_name)
            # DB storing logic here

x = len(game_titles)
for b in range(x):
    print(game_titles[b-1])