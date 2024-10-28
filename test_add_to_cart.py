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

#kiểm tra thêm sản phẩm vào giỏ hàng
def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(3)
    element=driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    q=element.text
    time.sleep(5)
    assert "1" in q

#kiểm tra thêm nhiều sản phẩm vào giỏ hàng
def test_add_multi_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    products_list=["cart-sauce-labs-backpack","cart-sauce-labs-bike-light","cart-sauce-labs-bolt-t-shirt","cart-sauce-labs-fleece-jacket","cart-sauce-labs-onesie","cart-test.allthethings()-t-shirt-(red)"]
    for p in products_list:
        time.sleep(3)
        driver.find_element(By.XPATH,f"//*[@id='add-to-{p}']").click()
        time.sleep(5)
    element=driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    q=element.text
    assert "6" in q

#kiểm tra thanh toán thành công
def test_checkout_successfully(driver):
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
    postcode=driver.find_element(By.XPATH,"//*[@id='postal-code']")
    postcode.send_keys("80000")
    driver.find_element(By.XPATH,"//*[@id='continue']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id='finish']").click()
    time.sleep(3)
    completed=driver.find_element(By.XPATH,"//*[@id='checkout_complete_container']/h2")
    assert "Thank you for your order!" in completed.text

#kiểm tra thanh toán thất bại 
def test_checkout_failed(driver):
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
    time.sleep(3)
    error=driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
    assert "Error: First Name is required" in error.text