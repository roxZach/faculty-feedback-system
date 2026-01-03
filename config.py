import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="openupnow",
    database="faculty_feedback"
)

cursor=db.cursor()