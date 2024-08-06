import os

project_structure = {
    "config": {
        "__init__.py": "",
        "config.py": """import os

class Config:
    SELENIUM_DRIVER_PATH = os.getenv('SELENIUM_DRIVER_PATH', '/path/to/driver')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com')
    DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING', 'database_connection_string')
    REPORT_PATH = os.getenv('REPORT_PATH', '/path/to/report')

config = Config()
"""
    },
    "src": {
        "__init__.py": "",
        "main.py": """from selenium import webdriver
from src.selenium.login_actions import login
from src.selenium.search_actions import search
from src.selenium.form_submission import submit_form
from src.api.api_client import APIClient
from src.database.db_connection import DatabaseConnection
from src.services.report_generator import generate_report
from config.config import config

def main():
    # Selenium Automation
    driver = webdriver.Chrome(config.SELENIUM_DRIVER_PATH)
    login(driver)
    search(driver, "example search term")
    submit_form(driver)
    driver.quit()
    
    # API Connection
    api_client = APIClient(base_url=config.API_BASE_URL)
    data = api_client.fetch_data()
    
    # Database Connection
    db = DatabaseConnection(config.DB_CONNECTION_STRING)
    db.connect()
    db.insert_data(data)
    db.close()
    
    # Generate Report
    generate_report(config.REPORT_PATH, data)

if __name__ == '__main__':
    main()
"""
    },
    "src/selenium": {
        "__init__.py": "",
        "browser_setup.py": "",
        "login_actions.py": """def login(driver):
    driver.get('http://example.com/login')
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    username.send_keys('your_username')
    password.send_keys('your_password')
    login_button = driver.find_element_by_name('login')
    login_button.click()
""",
        "search_actions.py": """def search(driver, query):
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(query)
    search_box.submit()
""",
        "form_submission.py": """def submit_form(driver):
    form_element = driver.find_element_by_name('form_element')
    form_element.send_keys('data')
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
""",
        "page_objects": {
            "__init__.py": "",
            "login_page.py": """from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.login_button_locator = (By.NAME, 'login')

    def enter_username(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()
"""
        }
    },
    "src/api": {
        "__init__.py": "",
        "api_client.py": """import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self):
        response = requests.get(f'{self.base_url}/data')
        return response.json()
""",
        "file_uploader.py": """import requests

class FileUploader:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload_file(self, file_path):
        with open(file_path, 'rb') as file:
            response = requests.post(f'{self.base_url}/upload', files={'file': file})
        return response.json()
""",
        "data_fetcher.py": """import requests

class DataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}')
        return response.json()
""",
        "auth_client.py": """import requests

class AuthClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        response = requests.post(f'{self.base_url}/login', data={'username': username, 'password': password})
        return response.json()

    def refresh_token(self, refresh_token):
        response = requests.post(f'{self.base_url}/refresh', data={'refresh_token': refresh_token})
        return response.json()
"""
    },
    "src/database": {
        "__init__.py": "",
        "db_connection.py": """import sqlite3

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
""",
        "queries.py": """def get_all_records_query():
    return "SELECT * FROM table_name"

def insert_data_query():
    return "INSERT INTO table_name (column1, column2) VALUES (?, ?)"
""",
        "models.py": """class DataModel:
    def __init__(self, column1, column2):
        self.column1 = column1
        self.column2 = column2

    def to_tuple(self):
        return (self.column1, self.column2)
""",
        "migrations": {
            "__init__.py": "",
            "create_tables.py": """def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    connection.commit()
"""
        }
    },
    "src/utils": {
        "__init__.py": "",
        "helpers.py": "",
        "logger.py": "",
        "file_utils.py": "",
        "data_processing.py": "",
        "email_utils.py": "",
        "json_utils.py": "",
    },
    "src/services": {
        "__init__.py": "",
        "report_generator.py": "",
        "notification_service.py": "",
        "scheduler.py": "",
    },
    "tests": {
        "__init__.py": "",
        "test_selenium.py": "",
        "test_api.py": "",
        "test_database.py": "",
        "test_utils.py": "",
        "test_services.py": "",
    },
    ".gitignore": "",
    "README.md": "",
    "requirements.txt": "",
    "setup.py": ""
}

def create_project_structure(base_path, structure):
    for name, content in structure.items():
        if isinstance(content, dict):
            dir_path = os.path.join(base_path, name)
            os.makedirs(dir_path, exist_ok=True)
            create_project_structure(dir_path, content)
        else:
            file_path = os.path.join(base_path, name)
            with open(file_path, 'w') as file:
                file.write(content)

# Create the project structure
base_path = 'project_name'  # Change this to your desired project folder name
os.makedirs(base_path, exist_ok=True)
create_project_structure(base_path, project_structure)
