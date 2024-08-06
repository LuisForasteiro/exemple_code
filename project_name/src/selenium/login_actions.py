def login(driver):
    driver.get('http://example.com/login')
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    username.send_keys('your_username')
    password.send_keys('your_password')
    login_button = driver.find_element_by_name('login')
    login_button.click()
