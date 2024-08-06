from selenium import webdriver
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
