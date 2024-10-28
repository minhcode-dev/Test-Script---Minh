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

#kiểm tra các liên kết bị hỏng 
def test_nav(driver):
    #truy cập trang và đăng nhập
    driver.get("https://www.saucedemo.com/")
    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    #tìm hết các phần tử có tag là a 
    links = driver.find_elements(By.TAG_NAME, "a")
    original_window = driver.current_window_handle
    #vòng lặp qua links tìm thuộc tính href
    for link in links:
        href = link.get_attribute("href")
        if not href or "#" in href:
            continue
        #mở một tab mới với href được truyền vào
        driver.execute_script("window.open(arguments[0]);", href)
        #chuyển trang cuối cùng
        driver.switch_to.window(driver.window_handles[-1])
        try:
            driver.get(href)
            assert driver.title != "", f"Link {href} không tải được."
        except WebDriverException as e:
            print(f"Lỗi khi tải link {href}: {e}")
        finally:
            driver.close()
            driver.switch_to.window(original_window)