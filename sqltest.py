import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "3k.sqlite")

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cursor = cur.execute('SELECT Column1, Column2 FROM list1')
for row in cursor:
    print(row)
    print(list(row))

conn.close()