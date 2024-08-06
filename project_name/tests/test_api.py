import unittest
from src.api.api_client import APIClient
from src.api.auth_client import AuthClient
from config.config import config

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient(config.API_BASE_URL)
    
    def test_fetch_data(self):
        response = self.client.fetch_data()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)

class TestAuthClient(unittest.TestCase):
    def setUp(self):
        self.client = AuthClient(config.API_BASE_URL)
    
    def test_login(self):
        response = self.client.login('username', 'password')
        self.assertIn('token', response)
    
    def test_refresh_token(self):
        response = self.client.refresh_token('some_refresh_token')
        self.assertIn('token', response)

if __name__ == '__main__':
    unittest.main()
