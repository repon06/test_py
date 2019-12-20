'''
# driver = webdriver.Chrome()
driver = DriverFactory().get_web_driver("chrome")
# driver = webdriver.Chrome('/path/to/chromedriver')

driver.get("http://www.google.com")

elem = driver.find_element_by_name("q")
elem.send_keys("Hello WebDriver!")
elem.submit()

print(driver.title)
driver.close()
'''