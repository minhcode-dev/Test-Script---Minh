import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,requests
from selenium.common.exceptions import WebDriverException

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_data_check_out_product(driver):
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
    itemtotal_text=driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[6]").text
    item_total = float(itemtotal_text.replace("Item total: $", ""))
    tax_text=driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[7]").text
    tax = float(tax_text.replace("Tax: $", ""))
    total = item_total + tax
    print(total)
    final_total_text = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
    final_total = float(final_total_text.replace("Total: $", ""))
    print(final_total)
    assert final_total == total, f"Tổng số tiền không chính xác: {final_total} (mong đợi: {total})"

def test_data_check_out_products(driver):
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
    itemtotal_text=driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[6]").text
    item_total = float(itemtotal_text.replace("Item total: $", ""))
    tax_text=driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[7]").text
    tax = float(tax_text.replace("Tax: $", ""))
    total = item_total + tax
    print(total)
    final_total_text = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
    final_total = float(final_total_text.replace("Total: $", ""))
    print(final_total)
    assert final_total == total, f"Tổng số tiền không chính xác: {final_total} (mong đợi: {total})"