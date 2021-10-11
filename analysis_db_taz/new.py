import sqlite3
import csv

# Create database connection to an in-memory database
taz_db = sqlite3.connect(":memory:")

# Obtain a cursor object
cursorob = taz_db.cursor()

# Create a table in the in-memory database
createTable = "CREATE TABLE vendas(nped int,cliente varchar(200),data int,codprod int,qdd real,preco real)"
cursorob.execute(createTable)

# Opening CSV data File
a_file = open(f'/Users/gabrielreus/Downloads/merged.csv')
rows = csv.reader(a_file)

# Insert data into DB
data = "INSERT INTO vendas VALUES (nped,cliente,data,codprod,qdd,preco)"
cursorob.executemany(data, rows)
cursorob.execute("SELECT * FROM vendas")
print (cursorob.fetchall())
