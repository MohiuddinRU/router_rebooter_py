from selenium.webdriver.common.by import By

from router_rebooter.reboot_router import get_base_url, get_reboot_url, login


def test_login_navigates_to_router_base_url():
    driver = login()
    driver.get.assert_any_call(get_base_url())


def test_login_page_has_username_and_password_input():
    driver = login()
    driver.find_element.assert_any_call(By.ID, "login_input_username")
    driver.find_element.assert_any_call(By.ID, "login_input_password")
    print("hello")


def test_login_clicks_login_button():
    driver = login()
    driver.find_element.assert_any_call(By.ID, "login_button")


def test_navigates_to_reboot_page():
    driver = login()
    driver.get.assert_any_call(get_reboot_url())
