# Selenium Test Scripts

## Mô tả:
đây là các test script dành cho trang web https://www.saucedemo.com/ về việc kiểm tra đăng nhập, thêm sản phẩm vào giỏ hàng, thanh toán, sắp xếp sản phẩm, responsive, tính hợp lệ của dữ liệu.
tổng cộng 26 hàm cho các chức năng trên 
## Yêu cầu: 
- Python 3.x
- Trình điều khiển Selenium (ChromeDriver, EdgeDriver, v.v.)
- Thư viện Python: `selenium`, `pytest`

## Hướng dẫn thiết lập môi trường
### Bước 1: Cài đặt Python
nếu chưa có python, hãy cài đặt Python tại (https://www.python.org/downloads/).
### Bước 2: Tạo môi trường ảo (tùy chọn)
Để tránh xung đột giữa các thư viện, bạn có thể tạo một môi trường ảo. Chạy các lệnh sau trong terminal:
```bash
# Cài đặt virtualenv nếu chưa có
pip install virtualenv

# Tạo môi trường ảo
virtualenv venv

# Kích hoạt môi trường ảo
# Trên Windows
venv\Scripts\activate

# Trên macOS/Linux
source venv/bin/activate

## cài đặt selenium 
nếu chưa có, hãy cài đặt selenium tại https://selenium-python.readthedocs.io/installation.html#downloading-selenium-server
sau khi tải xong thì thêm vào path


Để chạy riêng lẻ từng script ta dùng lệnh: pytest + tên test muốn chạy
Để chạy tất cả các script ta dùng lệnh: pytest -v 
