import mysql.connector
from mysql.connector import Error

def get_connection():
    hostname = "2tgpcr.h.filess.io"
    database = "db_akademik_hallyeswe"
    port = "3305"
    username = "db_akademik_hallyeswe"
    password = "b0bc81f04962bb99b28074a8201d704c862812df"

    try:
        connection = mysql.connector.connect(
            host=hostname, 
            database=database, 
            user=username, 
            password=password, 
            port=port
        )
        if connection.is_connected():
            return connection
            
    except Error as e:
        print("Error while connecting to MariaDB", e)
        return None
