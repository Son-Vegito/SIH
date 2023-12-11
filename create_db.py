import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password'
)

cursorObj=dataBase.cursor()

cursorObj.execute('create database AICTE_db')

print('Database Created')