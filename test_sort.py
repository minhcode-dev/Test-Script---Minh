import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,requests
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

#kiểm tra sắp xếp theo tên từ z-a
def test_sort_name_z_a(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    select=Select(driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select"))
    selected=select.select_by_value("za")
    time.sleep(2)
    products = driver.find_elements(By.XPATH, "//*[@id='inventory_container']")
    product_names = [product.text for product in products]
    assert product_names == sorted(product_names, reverse=True)

#kiểm tra sắp xếp theo tên từ a-z
def test_sort_name_a_z(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    select=Select(driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select"))
    selected=select.select_by_value("az")
    time.sleep(2)
    products = driver.find_elements(By.XPATH, "//*[@id='inventory_container']")
    product_names = [product.text for product in products]
    assert product_names == sorted(product_names)

#kiểm tra sắp xếp theo giá cao đến thấp
def test_sort_price_high_low(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    select=Select(driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select"))
    selected=select.select_by_value("hilo")
    product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace("$", "")) for price in product_prices]
    print(f"{prices} and {sorted(prices,reverse=True)}")
    assert prices==sorted(prices,reverse=True),f"Giá không được sắp xếp đúng: {prices}"

#kiểm tra sắp xếp theo giá thấp đến cao
def test_sort_price_low_high(driver):
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    select=Select(driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select"))
    selected=select.select_by_value("lohi")
    product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace("$", "")) for price in product_prices]
    print(f"{prices} and {sorted(prices)}")
    assert prices==sorted(prices),f"Giá không được sắp xếp đúng: {prices}"


