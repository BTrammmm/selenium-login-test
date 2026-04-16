class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, keyword):
        box = self.driver.find_element("name", "q")
        box.send_keys(keyword)
        box.submit()
