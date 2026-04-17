from pages.login_page import LoginPage
from utils.driver_setup import get_driver

def test_login_success():
    driver = get_driver()
    login = LoginPage(driver)

    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in login.get_message()

    driver.quit()
