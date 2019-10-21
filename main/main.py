import json
import urllib3.request


url = "https://store.playstation.com/valkyrie-api/ru/RU/999/container/STORE-MSF75508-FULLGAMES?sort=release_date&direction=desc&size=30&bucket=games&start=0"
http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.status)
# print(r.data)

json_string = r.data

data = json.loads(json_string)

# print(type(data))
# print(data['included'])

full_list = data['included']
print(type(full_list))

length = len(full_list)


for i in range(length):
    print(i)
    element = full_list[i]
    type1 = full_list[i]['type']
    print(type(element))
    print(type1)