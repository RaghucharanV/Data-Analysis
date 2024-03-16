import sqlite3
import csv

#create db
conn = sqlite3.connect('scrapy.db')

#create conn
cur= conn.cursor()

#create table world_population
cur.execute("CREATE TABLE if not exists world_population(country TEXT ,Population TEXT,yearly_change TEXT,Net_change TEXT,Density INTEGER,Land_Area TEXT,Migrants TEXT,Fert_Rate TEXT,Med_Age INTEGER,Urban_Pop TEXT,World_share TEXT)")


#after scraping data csv to db table.
with open('output.csv', 'r',newline='',encoding='utf-8') as csvfile:
    csvfile = csv.DictReader(csvfile)
    for row in csvfile:
        cur.execute("INSERT INTO world_population VALUES (?,?,?,?,?,?,?,?,?,?,?)",(row['country '],row['Population'],row['yearly change'],row['Net change'],row['Density'],row['Land Area (Km2)'],row['Migrants(n)'],row['Fert_Rate'],row['Med_Age'],row['Urban_Pop'],row['World_share']))

    conn.commit()

# check data
print(cur.execute("select * from world_population limit 10").fetchall())


#close conn
conn.close()