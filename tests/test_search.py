from pages.search_page import SearchPage

def test_search(driver):
    driver.get("https://google.com")

    search = SearchPage(driver)
    search.search("Selenium Python")
