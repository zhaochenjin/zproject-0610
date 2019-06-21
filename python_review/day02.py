import mysql.connector
from collections import Iterable

config = {'user':'root', 'password':'123456'}

connection = mysql.connector.connect(**config)

print(connection)

cursor = connection.cursor()

cursor.execute('show databases')

print(isinstance(cursor, Iterable))

for db in cursor:
    print(db)

print('-------------')

cursor.execute('select * from douban.movies')

rows = cursor.fetchall()

for row in rows:
    print(row)