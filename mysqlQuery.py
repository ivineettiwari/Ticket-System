import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',  # Replace 'your_host' with the MySQL host
            database='testdb',  # Replace 'your_database' with the name of your database
            user='root',  # Replace 'your_username' with your MySQL username
            password='vineet123',  # Replace 'your_password' with your MySQL password
            port=3307
        )
        
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Failed to connect to MySQL database")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def select_query(connection):
    try:
        # Execute SELECT query
        cursor = connection.cursor()
        query = "SELECT * FROM person;"  # Replace 'your_table' with the name of your table
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Display the results
        print("SELECT query results:")
        for row in rows:
            print(row)

    except Error as e:
        print(f"Error executing SELECT query: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Connect to MySQL
connection = connect_to_mysql()

# Execute SELECT query
if connection:
    select_query(connection)
else:
    print("Connection to MySQL failed, SELECT query cannot be executed")