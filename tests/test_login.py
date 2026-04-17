from pages.login_page import LoginPage

def test_login(driver):
    driver.get("https://example.com/login")

    login = LoginPage(driver)
    login.login("admin", "123456")
