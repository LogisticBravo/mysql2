import pymysql
import os

#Get username from workspace
#(Modify this variable if running on another environment)

username = os.getenv('C9_User')

#connect to database
connection = pymysql.connect(host = 'localhost',
user = username,
password ='',
db="Chinook")

try:
    #run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection, regardless of whether the above was successful
    connection.close()
    