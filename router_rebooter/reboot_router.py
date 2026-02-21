import os
from unittest.mock import MagicMock, patch

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()


@pytest.fixture
def mock_driver():
    with patch("router_rebooter.reboot_router.webdriver.Chrome") as mock_chrome:
        driver = MagicMock()
        mock_chrome.return_value = driver
        yield driver


def get_username():
    return os.getenv("ROUTER_USERNAME")


def get_password():
    return os.getenv("ROUTER_PASSWORD")


def get_base_url():
    return os.getenv("ROUTER_URL")


def get_reboot_url():
    return os.getenv("REBOOT_URL")


def get_status_url():
    return os.getenv("STATUS_URL")


def navigate_to_login_page():
    driver = webdriver.Chrome()
    driver.get(get_base_url())
    return driver


def login():
    driver = navigate_to_login_page()
    driver.find_element(By.ID, "login_input_username").send_keys(get_username())
    driver.find_element(By.ID, "login_input_password").send_keys(get_password())
    driver.find_element(By.ID, "login_button").click()

    return driver


def reboot_router(driver):
    pass
