import requests
import time
import json
def connect_bungie(url, file):
    HEADERS = {"X-API-Key":'02929adf4cdf4e78a1fd9c35c7a9086b'}
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    with open(file, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    res = response.json()['ErrorStatus']
    return res
res = connect_bungie('https://www.bungie.net/Platform/Destiny2/3/Profile/4611686018522422927/Character/2305843010031474019/?components=201', 'files\character.json'  )
if res == "Success":
    print("Connecting to Bungie")
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('Searching and downloading character')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('Connected')
    print('Downloading DataBase')
    db = connect_bungie('https://www.bungie.net/Platform/Destiny2/Manifest/', 'files\manifest.json')
    print(db)
    
else:
    print('Error: ', res)
    
print('* '*28)

print()