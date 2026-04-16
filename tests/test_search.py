from selenium import webdriver
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search = driver.find_element("name", "q")
    search.send_keys("Selenium Python")
    search.submit()

    time.sleep(2)
    assert "Selenium" in driver.title

    driver.quit()
