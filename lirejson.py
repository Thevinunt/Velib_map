# open file belib.json
import json
from optparse import Values

with open('belib.json') as json_data:
    data_dict=json.load(json_data)
    print(data_dict)
   # print(data_dict)
for item in data_dict:
    # print(item)
    print(item)
    print(item['nom_station'])
    print(item['coordonneesxy'])
    print(item['coordonneesxy']["lon"])
    print(item['coordonneesxy']["lat"])

#connect to mysql

Base_name='yutopia'
table_name="t_marker"

import mysql.connector
from mysql.connector import Error

try:

    connection = mysql.connector.connect(host='localhost',

                                         database=Base_name,

                                         user='root',

                                         password='')

    if connection.is_connected():
        print("Connected to MySQL Server version ")



except Error as e:

    print("Error while connecting to MySQL", e)

#insert data in table

cursor= connection.cursor()

for item in data_dict:

    sql = "INSERT INTO "+table_name+" (nom_marker, latitude_marker, longitude_marker) VALUES (%s, %s, %s)"
    val = (item['nom_station'], item['coordonneesxy']["lon"], item['coordonneesxy']["lat"])
    cursor.execute(sql, val)
    connection.commit()