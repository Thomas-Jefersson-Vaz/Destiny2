import sqlite3
import json
import requests
import html
import time
# Caminho para o arquivo JSON temporário
file = r'files/temp.json'
# Definindo a variável found_object como global
found_object = None

# Função para conectar à API da Bungie e salvar os dados em um arquivo JSON
def connect_bungie(url, file):
    HEADERS = {"X-API-Key":'02929adf4cdf4e78a1fd9c35c7a9086b'}
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    
    # Salva os dados no arquivo JSON
    with open(file, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        
    # Retorna o status de erro da resposta da API
    res = response.json()['ErrorStatus']
    return res

# Retorna o status de erro da resposta da API
def find_char_class():
    with open(r'files/character.json', 'r') as json_file:
        hash = json.load(json_file)
    target_hash = int(hash['Response']['character']['data']['classHash'])
    return target_hash

# Função para limpar o arquivo temporário
def clear_temp_file():
    empty = ''
    with open(r'files/temp.json', 'w') as json_file:
        data = json.dump(empty, json_file)
        return data

# Função para obter dados da base de dados SQLite
def pull_data():
    db_file = r'database.content'
    conn = sqlite3.connect(db_file)

    cursor = conn.cursor()
    cursor.execute('SELECT json FROM DestinyClassDefinition')
    rows = cursor.fetchall()

    data_list = []

    for row in rows:
        json_data = row[0]
        data_list.append(json.loads(json_data))
    # Salva os dados no arquivo JSON
    with open(file, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)
    
    conn.close()

# Carrega os dados do arquivo JSON
with open(file, 'r') as json_file:
    data = json.load(json_file)
    

# Função para mostrar o resultado com base no hash da classe
def show_result():
    global found_object
    # Encontra o hash da classe do personagem
    target_hash = find_char_class()
    for obj in data:
        if obj.get("hash") == target_hash:
            found_object = obj
            break
    if found_object:
        found_name = found_object['displayProperties']['name']
        decoded_name = html.unescape(found_name)
        print("Classe: ",decoded_name)
    else:
        print("Object with hash", target_hash, "not found.")  

def timing():
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)