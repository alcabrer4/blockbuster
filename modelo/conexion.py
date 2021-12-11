import mysql.connector

cnx = mysql.connector.connect(user='a', password='12345',
                              host='127.0.0.1',
                              database='blockbuster')

cnx.close()