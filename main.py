import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'example_schema', password = 'SQL.12454933')

cursor = connection.cursor()

testQuery = ("SELECT * FROM example_table")

cursor.execute(testQuery)

for item in cursor:
    print(item)



connection.commit()
cursor.close()
connection.close()