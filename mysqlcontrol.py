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

def transaction_query(connection):
    try:
        # Start a MySQL transaction
        cursor = connection.cursor()

        # Begin the transaction
        cursor.execute("START TRANSACTION")

        # SELECT query
        select_query = "SELECT * FROM person"  # Replace 'your_table' with the name of your table
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print("SELECT query results:")
        insert_data = []
        for row in rows:
            insert_data.append(row)

        # INSERT query
        print(insert_data)
        insert_query = "INSERT INTO person_history (idperson, personName, personAdress, personCity) VALUES" + ",".join("(%s, %s,%s, %s)" for _ in insert_data)  # Replace 'your_table' and 'column1', 'column2' with your table and column names
        flattened_values = [item for sublist in insert_data for item in sublist]
        cursor.execute(insert_query, flattened_values)
        print("INSERT query executed successfully")

        # DELETE query
        delete_query = "DELETE FROM person"  # Replace 'your_table' with the name of your table and 'condition' with your deletion condition
        cursor.execute(delete_query)
        print("DELETE query executed successfully")

        # Commit the transaction
        connection.commit()
        print("Transaction committed successfully")

    except Error as e:
        # Rollback the transaction if an error occurs
        connection.rollback()
        print(f"Transaction rolled back due to error: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Connect to MySQL
connection = connect_to_mysql()

# Execute transaction query
if connection:
    transaction_query(connection)
else:
    print("Connection to MySQL failed, transaction query cannot be executed")
