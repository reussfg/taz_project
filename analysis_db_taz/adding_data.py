import sqlite3
import csv

conn = sqlite3.connect(r'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/db_read/clean/taz_db')
cur = conn.cursor()

year = [x for x in range(2010, 2022)]
for k in year:
    with open(f'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/db_read/clean/{k}-clean.csv', 'r') as f:
        csv_reader = csv.reader(f)
        cur.executemany('''INSERT INTO vendas VALUES (nped,cliente,data,codprod,prod,qtd,preco)''', csv_reader)

