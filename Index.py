import funcoes
arcano_teste = 'https://www.bungie.net/Platform/Destiny2/3/Profile/4611686018522422927/Character/2305843010031474019/?components=200'
titan_teste = 'https://www.bungie.net/Platform/Destiny2/3/Profile/4611686018522422927/Character/2305843010489294101/?components=200'
res = funcoes.connect_bungie(titan_teste, r'files/character.json'  )

if res == "Success":
    print("Connecting to Bungie")
    funcoes.timing()
    print('Searching and downloading character')
    funcoes.timing()
    print('Connected')
    print('Downloading DataBase')
    db = funcoes.connect_bungie('https://www.bungie.net/Platform/Destiny2/Manifest/', r'files/manifest.json')
    print(db)
    
else:
    print('Error: ', res)
    
print('* '*28)
print()