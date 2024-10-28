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
    
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]")
        assert login_button.is_displayed(), f"Nút đăng nhập không hiển thị trên kích thước {width}x{height}"

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