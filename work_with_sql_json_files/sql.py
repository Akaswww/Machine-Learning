# connect to yur database and read data from your database using xampp and

# u need to install a library called "mysql.connector" which connects python to your database
# import mysql.connector

# import pandas as pd

# conn= mysql.connector.connect(host='127.0.0.1',port=3306,user='Akash',password='abbuakash',database='world')

# df=pd.read_sql_query("SELECT * FROM city",conn)
# print(df.head())

import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',     # Use IP not 'localhost' to avoid socket confusion
        port=3306,
        user='Akash',
        password='abbuakash',
        database='world'
    )
    if conn.is_connected():
        print("Successfully connected to MySQL database")
        # Do your DB operations here

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection is closed")


