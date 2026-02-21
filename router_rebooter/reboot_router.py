import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


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


def wait_until(driver, byId, selector, timeout=30):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_any_elements_located((byId, selector))
    )[0]


def login():
    driver = webdriver.Chrome()
    driver.get(get_base_url())

    wait_until(driver, By.ID, "login_input_username")
    driver.find_element(By.ID, "login_input_username").send_keys(get_username())

    wait_until(driver,By.ID, "login_input_password")
    driver.find_element(By.ID, "login_input_password").send_keys(get_password())

    wait_until(driver, By.ID, "login_button")
    driver.find_element(By.ID, "login_button").click()

    driver.get(get_reboot_url())

    wait_until(driver, By.ID, "reboot_restart_button")
    driver.find_element(By.ID, "reboot_restart_button").click()

    confirm_xpath = "//button//span[contains(text(), 'Confirm')]/parent::button"
    wait_until(
        driver,
        By.XPATH,
        confirm_xpath
    )
    driver.find_element(By.XPATH, confirm_xpath).click()

    return driver

if __name__ == "__main__":
    driver = login()
