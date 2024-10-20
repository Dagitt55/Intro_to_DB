import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Replace with your MySQL server hostname
            user="root",   # Replace with your MySQL username
            password="password" # Replace with your MySQL password
        )
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Incorrect username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
