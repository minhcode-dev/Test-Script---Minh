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
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#kiểm tra tương thích với trang đăng nhập
def test_responsive_design_login(driver):
    # Mở trang
    driver.get("https://www.saucedemo.com/")
    
    # Danh sách kích thước màn hình cần kiểm tra
    screen_sizes = [
        (390, 844),   #iphone 12
        (430, 932),  #iphone 14 promax
        (768, 1024),  # tablet
        (1366, 768),  # laptop
        (1920, 1080)  # pc
    ]
    #vòng lập qua chiều dài và cao để đặt cho trang 
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        login = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]")
        assert login.is_displayed(), f"Nút đăng nhập không hiển thị trên kích thước {width}x{height}"

#kiểm tra tương thích với trang sản phẩm
def test_responsive_design_products(driver):
    driver.get("https://www.saucedemo.com/")
    screen_sizes = [
        (390, 844),   #iphone 12
        (430, 932),  #iphone 14 promax
        (768, 1024),  # tablet
        (1366, 768),  # laptop
        (1920, 1080)  # pc
    ]
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        products=driver.find_element(By.ID,"inventory_container")
        assert products.is_displayed(), f"Nút đăng nhập không hiển thị trên kích thước {width}x{height}"

#kiểm tra tương thích cho trang giỏ hàng
def test_responsive_design_cart(driver):
    driver.get("https://www.saucedemo.com/")
    screen_sizes = [
        (390, 844),   #iphone 12
        (430, 932),  #iphone 14 promax
        (768, 1024),  # tablet
        (1366, 768),  # laptop
        (1920, 1080)  # pc
    ]
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        products=driver.find_element(By.ID,"cart_contents_container")
        assert products.is_displayed(), f"Nút đăng nhập không hiển thị trên kích thước {width}x{height}"

#kiểm tra tương thích cho trang điền thông tin giỏ hàng
def test_responsive_design_cart_inf(driver):
    driver.get("https://www.saucedemo.com/")
    screen_sizes = [
        (390, 844),   #iphone 12
        (430, 932),  #iphone 14 promax
        (768, 1024),  # tablet
        (1366, 768),  # laptop
        (1920, 1080)  # pc
    ]
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)
    driver.find_element(By.ID,"checkout").click()
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        products=driver.find_element(By.ID,"checkout_info_container")
        assert products.is_displayed(), f"Nút đăng nhập không hiển thị trên kích thước {width}x{height}"

#kiểm tra tương thích cho trang tổng thanh toán
def test_responsive_design_checkout_summary(driver):
    driver.get("https://www.saucedemo.com/")
    screen_sizes = [
        (390, 844),   #iphone 12
        (430, 932),  #iphone 14 promax
        (768, 1024),  # tablet
        (1366, 768),  # laptop
        (1920, 1080)  # pc
    ]
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
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
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        products=driver.find_element(By.ID,"checkout_summary_container")
        assert products.is_displayed(), f"Nút đăng nhập không hiển thị trên kích thước {width}x{height}"