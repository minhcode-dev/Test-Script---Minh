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
#kiểm tra đăng nhập thành công
def test_login_successfully(driver):
    driver.get("https://www.saucedemo.com/") #truy cập vào trang 
    #nhập username và password
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    #nhấn login
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)
    link="https://www.saucedemo.com/inventory.html"
    #kiểm tra xem đăng nhập thành công hay không thông qua liên kết hiện tại
    assert link in driver.current_url

#kiểm tra đăng xuất
def test_logout(driver):
    #truy cập trang và đăng nhập
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    #tìm menu có đăng xuất và nhấn đăng xuất
    driver.find_element(By.ID,"react-burger-menu-btn").click()
    time.sleep(3)
    driver.find_element(By.ID,"logout_sidebar_link").click()
    time.sleep(3)
    # kiểm tra điều hướng trang có về lại trang đăng nhập chưa ?
    link="https://www.saucedemo.com/"
    assert link in driver.current_url

#kiểm tra đăng nhập khi bỏ trống user và password
def test_empty_user_pass(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Epic sadface: Username is required" in error_message

#kiểm tra đăng nhập thất bại
def test_login_failed(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message