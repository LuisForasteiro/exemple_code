def submit_form(driver):
    form_element = driver.find_element_by_name('form_element')
    form_element.send_keys('data')
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
