import json
import urllib3.request

url = "https://store.playstation.com/valkyrie-api/ru/RU/999/container/STORE-MSF75508-FULLGAMES?sort=release_date&direction=desc&size=30&bucket=games&start=0"
http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.status)

json_string = r.data
data = json.loads(json_string)

full_list = data['included']
length = len(full_list)

for i in range(length):
    element = full_list[i]
    element_type = full_list[i]['type']
    if element_type == 'game':
        game_name = element['attributes']['name']
        print(game_name)
