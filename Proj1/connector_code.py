import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",               
    password="root123", 
    database="blog_db"  
)

cursor = conn.cursor()
print("Connected to MySQL")

cursor.close()
conn.close()