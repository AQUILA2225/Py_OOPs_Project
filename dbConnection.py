import mysql.connector

dbcon = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "ecom"
)

print("Database Connected Successfully!!!")
cursorObj = dbcon.cursor()