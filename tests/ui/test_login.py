from pages.login_page import LoginPage

def test_login_valid_user(driver, config):
    driver.get(config["url"])
    login = LoginPage(driver)
    login.login(config["username"], config["password"])
    assert "Dashboard" in driver.title
