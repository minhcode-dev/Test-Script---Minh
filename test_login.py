import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_successfully(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)
    link="https://www.saucedemo.com/inventory.html"
    assert link in driver.current_url

def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    driver.find_element(By.ID,"react-burger-menu-btn").click()
    time.sleep(3)
    driver.find_element(By.ID,"logout_sidebar_link").click()
    time.sleep(3)
    link="https://www.saucedemo.com/"
    assert link in driver.current_url

def test_empty_user_pass(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Epic sadface: Username is required" in error_message

def test_login_failed(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message