import sqlite3
import csv

# Connecting to the DB
conn = sqlite3.connect('taz_db')
cur = conn.cursor()

# Creating Table
createTable = "CREATE TABLE vendas (nped INTEGER,cliente TEXT,datas INTEGER,codprod INTEGER, qtd REAL, preco REAL)"
cur.execute(createTable)

# Opening CSV data File
a_file = open(f'/Users/gabrielreus/Downloads/merged.csv')
rows = csv.reader(a_file)

# Insert data into DB
data = "INSERT INTO vendas VALUES (?, ?, ?, ?, ?, ?)"
cur.executemany(data, rows)
cur.execute("SELECT * FROM vendas")
print (cur.fetchall())

# Close Connection
conn.commit()
conn.close()


