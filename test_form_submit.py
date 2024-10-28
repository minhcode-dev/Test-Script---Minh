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

def test_form_submit(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)
    link="https://www.saucedemo.com/inventory.html"
    assert link in driver.current_url

def test_form_submit_failed(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("@sa")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    error_mess=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_mess

def test_form_submit_locked(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("locked_out_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    error_mess=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
    assert "Epic sadface: Sorry, this user has been locked out." in error_mess

def test_form_checkout_failed_fn(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)
    driver.find_element(By.ID,"checkout").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='continue']").click()
    error=driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
    assert "Error: First Name is required" in error.text

def test_form_checkout_failed_ln(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)
    driver.find_element(By.ID,"checkout").click()
    time.sleep(3)
    firstname=driver.find_element(By.XPATH,"//*[@id='first-name']")
    firstname.send_keys("ab")
    driver.find_element(By.XPATH,"//*[@id='continue']").click()
    error=driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
    assert "Error: Last Name is required" in error.text

def test_form_checkout_failed_pc(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)
    driver.find_element(By.ID,"checkout").click()
    time.sleep(3)
    firstname=driver.find_element(By.XPATH,"//*[@id='first-name']")
    firstname.send_keys("ab")
    lastname=driver.find_element(By.XPATH,"//*[@id='last-name']")
    lastname.send_keys("cd")
    driver.find_element(By.XPATH,"//*[@id='continue']").click()
    error=driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
    assert "Error: Postal Code is required" in error.text