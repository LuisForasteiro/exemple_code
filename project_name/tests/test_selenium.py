import unittest
from selenium import webdriver
from src.selenium.page_objects.login_page import LoginPage
from config.config import config

class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(config.SELENIUM_DRIVER_PATH)
    
    def test_login(self):
        self.driver.get('http://example.com/login')
        login_page = LoginPage(self.driver)
        login_page.enter_username('your_username')
        login_page.enter_password('your_password')
        login_page.click_login()
        self.assertIn("Dashboard", self.driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
