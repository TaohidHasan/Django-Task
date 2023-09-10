import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password123'

	)

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE cruddatabase")

print("All Done!")