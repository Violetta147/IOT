# Cập nhật 1 — Tự làm mới thời tiết

## Mục tiêu

Chương trình tiếp tục chạy và tự lấy thời tiết của thành phố đã chọn sau mỗi khoảng thời gian, mặc định 10 phút.

## Thực hiện

1. Tách bước đổi tên thành phố thành tọa độ khỏi bước lấy thời tiết. Chỉ gọi Geocoding API một lần khi bắt đầu; mỗi chu kỳ sau chỉ gọi Current Weather API.
2. Thêm biến cấu hình khoảng cách giữa các lần cập nhật. Lấy dữ liệu ngay khi khởi động, sau đó chờ đủ thời gian mới gọi tiếp.
3. In thời điểm cập nhật, nhiệt độ và độ ẩm; điều chỉnh LED theo dữ liệu mới. Khi không lấy được dữ liệu, báo lỗi, tắt LED và chờ tới chu kỳ tiếp theo.
4. Cho phép dừng bằng `Ctrl+C`; tắt LED và giải phóng GPIO khi thoát.
5. Cập nhật README và kiểm thử bằng API, đồng hồ và GPIO giả.

## Hoàn thành khi

- Dữ liệu được cập nhật đúng chu kỳ mà không gọi API liên tục.
- Các chu kỳ của cùng một thành phố không gọi lại Geocoding API.
- LED phản ánh dữ liệu mới; lỗi tải dữ liệu làm LED tắt.
