import os

class Config:
    SELENIUM_DRIVER_PATH = os.getenv('SELENIUM_DRIVER_PATH', '/path/to/driver')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com')
    DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING', 'database_connection_string')
    REPORT_PATH = os.getenv('REPORT_PATH', '/path/to/report')

config = Config()
