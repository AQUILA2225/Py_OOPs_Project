
import mysql.connector

conObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        # auth_plugin="mysql_native_password",
        database="bankdb"
    )

print("✅ Database Connected Successfully")
cursorObj = conObj.cursor()