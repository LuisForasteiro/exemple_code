import unittest
from src.database.db_connection import DatabaseConnection
from src.database.migrations.create_tables import create_tables
from config.config import config

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnection(config.DB_CONNECTION_STRING)
        self.db.connect()
        create_tables(self.db.connection)
    
    def test_insert_data(self):
        cursor = self.db.connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'pass1')")
        self.db.connection.commit()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        self.assertEqual(len(data), 1)
    
    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()
