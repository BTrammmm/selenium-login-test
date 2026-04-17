from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    search_box = (By.NAME, "q")

    def search(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword)
