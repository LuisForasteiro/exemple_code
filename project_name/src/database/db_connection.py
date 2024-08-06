import sqlite3

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.connection_string)

    def insert_data(self, data):
        cursor = self.connection.cursor()
        cursor.executemany("INSERT INTO table_name VALUES (?, ?)", data)
        self.connection.commit()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()
