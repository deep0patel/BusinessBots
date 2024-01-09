import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class sql_database_manager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(sql_database_manager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.host = os.getenv("sql_host_name")
        self.user = os.getenv("sql_user_name")
        self.password = os.getenv("sql_password")
        self.database = os.getenv("sql_database_name")
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL database")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                print(cursor.statement)

            return cursor
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None

    def create(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(data.values())
        cursor = self.execute_query(query, values)
        if cursor:
            self.connection.commit()
            print(f"Inserted into {table_name} successfully")

    def read(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        cursor = self.execute_query(query)
        if cursor:
            return cursor.fetchall()
        return []

    def update(self, table_name, data, condition):
        update_values = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table_name} SET {update_values} WHERE {condition}"
        values = tuple(data.values())
        cursor = self.execute_query(query, values)
        if cursor:
            self.connection.commit()
            print(f"Updated {table_name} successfully")

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cursor = self.execute_query(query)
        if cursor:
            self.connection.commit()
            print(f"Deleted from {table_name} successfully")

# if __name__ == "__main__":
#     # Replace with your database credentials
#     db_manager = sql_database_manager(
#         host="localhost",
#         user="your_username",
#         password="your_password",
#         database="your_database_name"
#     )
#
#     db_manager.connect()
#
#     # Example usage:
#     # db_manager.create("users", {"username": "john_doe", "email": "john@example.com"})
#     # users = db_manager.read("users", "username = 'john_doe'")
#     # db_manager.update("users", {"email": "new_email@example.com"}, "username = 'john_doe'")
#     # db_manager.delete("users", "username = 'john_doe'")
#
#     db_manager.disconnect()
