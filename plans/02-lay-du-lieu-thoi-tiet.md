# Bước 2 — Lấy dữ liệu thời tiết

## Cần làm

1. Tạo dự án Python và khai báo thư viện HTTP trong tệp phụ thuộc. Đọc API key từ biến môi trường `OPENWEATHER_API_KEY`; không ghi key vào mã nguồn.
2. Nhận tên thành phố, loại bỏ khoảng trắng thừa và từ chối đầu vào rỗng. Cho phép thêm mã quốc gia nếu có nhiều thành phố trùng tên, ví dụ `Hanoi,VN`.
3. Gọi Geocoding API với tên thành phố và API key. Nếu không có kết quả, báo rằng không tìm thấy thành phố; nếu có nhiều kết quả, xác định cách chọn một địa điểm rõ ràng.
4. Dùng `lat`, `lon` để gọi Current Weather API với `units=metric`. Đặt thời gian chờ cho cả hai yêu cầu; kiểm tra mã phản hồi và đọc JSON.
5. Lấy `main.temp` (°C) và `main.humidity` (%), kiểm tra hai giá trị hợp lệ rồi trả về một cấu trúc dữ liệu đơn giản cho bước hiển thị và điều khiển LED.

## Hoàn thành khi

- Nhập một thành phố hợp lệ nhận được nhiệt độ và độ ẩm từ API bằng key riêng.
- Key thiếu, thành phố không tìm thấy, lỗi mạng hoặc JSON thiếu trường đều có thông báo phù hợp; không in API key ra màn hình hay log.

Nguồn kỹ thuật: [Geocoding API](https://openweathermap.org/api/geocoding-api), [Current Weather API](https://openweathermap.org/api/current).
