# Bước 2 — Lấy dữ liệu thời tiết

## Cần làm

1. Tạo dự án Python và khai báo thư viện HTTP trong tệp phụ thuộc. Đọc API key từ biến môi trường `OPENWEATHER_API_KEY`; không ghi key vào mã nguồn.
2. Nhận tên thành phố và loại bỏ khoảng trắng thừa. Có thể thêm mã quốc gia, ví dụ `Hanoi,VN`.
3. Gọi Geocoding API với tên thành phố và API key; lấy kết quả đầu tiên. Nếu không có kết quả, báo không tìm thấy thành phố.
4. Dùng `lat`, `lon` để gọi Current Weather API với `units=metric`. Đặt thời gian chờ cho cả hai yêu cầu; kiểm tra mã phản hồi và đọc JSON.
5. Lấy `main.temp` (°C) và `main.humidity` (%) để hiển thị và điều khiển LED.

## Hoàn thành khi

- Dữ liệu API giả cho một thành phố hợp lệ cho ra đúng nhiệt độ và độ ẩm.
- API key không nằm trong Git; kiểm tra với key thật khi có.

Nguồn kỹ thuật: [Geocoding API](https://openweathermap.org/api/geocoding-api), [Current Weather API](https://openweathermap.org/api/current).
