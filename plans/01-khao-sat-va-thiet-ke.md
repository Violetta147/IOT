# Bước 1 — Khảo sát và thiết kế

## Cần làm

1. Đọc mục 10, trang 125–127 của *Getting Started with Raspberry Pi* để ghi lại ý chính: gửi yêu cầu HTTP, dùng API key và đọc dữ liệu JSON. Khi truy cập được thư mục sách trên ổ `G:`, đối chiếu số trang và ví dụ trong bản sách đang dùng.
2. Xem [repo tham khảo](https://github.com/dothang13/lthtn2026_weather) khi truy cập được; chỉ lấy ý tưởng phù hợp, không sao chép API key hoặc phụ thuộc vào API cũ.
3. Chọn OpenWeather: dùng Geocoding API đổi tên thành phố thành tọa độ, rồi dùng Current Weather API lấy nhiệt độ và độ ẩm. Kiểm tra tài khoản/API key có gọi được hai API trước khi viết chương trình.
4. Xác nhận mẫu Raspberry Pi và linh kiện. Dự kiến nối LED qua điện trở hạn dòng vào GPIO17 (đánh số BCM) và GND; kiểm tra sơ đồ chân của thiết bị trước khi cắm.
5. Chốt quy tắc mẫu: nhiệt độ **dưới 30°C thì LED bật**, từ 30°C trở lên thì tắt. Ngưỡng sẽ thay đổi được bằng cấu hình.

## Hoàn thành khi

- Có API key dùng thử thành công và biết rõ các trường JSON cần đọc.
- Có sơ đồ nối LED đúng với Raspberry Pi thực tế và quy tắc bật/tắt đã được chốt.

Nguồn kỹ thuật: [Geocoding API](https://openweathermap.org/api/geocoding-api), [Current Weather API](https://openweathermap.org/api/current), [GPIO Zero](https://gpiozero.readthedocs.io/en/latest/).
