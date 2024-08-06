def search(driver, query):
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(query)
    search_box.submit()
