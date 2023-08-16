# import json
# manifest = 'files\manifest.json'
# with open(manifest) as file:
#     data = json.load(file)
# url = 'www.bungie.net'+data['Response']['mobileWorldContentPaths']['pt-br']
# print(url)

import sqlite3
from sqlite3 import Error
# con = sqlite3.connect('database.sqbpro')
# res = 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)


if __name__ == '__main__':
    create_connection(r'database.sqbpro')