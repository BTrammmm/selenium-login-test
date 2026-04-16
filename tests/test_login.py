import json
from pages.login_page import LoginPage

def load_data():
    with open("data/test_data.json") as f:
        return json.load(f)

def test_login_success(driver):
    data = load_data()
    user = data["valid_user"]

    page = LoginPage(driver)
    page.open()
    page.login(user["username"], user["password"])

    assert "secure" in driver.current_url


def test_login_fail(driver):
    data = load_data()
    user = data["invalid_user"]

    page = LoginPage(driver)
    page.open()
    page.login(user["username"], user["password"])

    assert "error" in driver.page_source
