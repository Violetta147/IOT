# Kế hoạch dự án

## Phiên bản hiện tại — luồng chính

- [x] Đối chiếu mục 10, trang 125–127 của *Getting Started with Raspberry Pi*.
- [x] Nhập thành phố, dùng API key lấy nhiệt độ và độ ẩm từ OpenWeather.
- [x] Hiển thị dữ liệu và bật/tắt LED theo ngưỡng nhiệt độ cấu hình được.
- [x] Viết hướng dẫn cài đặt, nối mạch và bảo vệ API key khỏi Git/log lỗi.
- [x] Chạy 7 kiểm thử tự động; thử API thật và GPIO giả trong Codespaces.
- [ ] Thử LED và GPIO trên Raspberry Pi thật.

## Phiên bản tiếp theo — theo dõi thời tiết

- [ ] Tự cập nhật dữ liệu sau khoảng thời gian cấu hình được (dự kiến 10–15 phút).
- [ ] Cho phép đổi thành phố khi chương trình đang chạy; chỉ tra lại tọa độ khi đổi thành phố.
- [ ] Cập nhật LED sau mỗi lần lấy dữ liệu; bổ sung hướng dẫn và kiểm thử cho luồng mới.

## Phiên bản sau — dữ liệu chứng khoán

- [ ] Chọn API chứng khoán, xác định mã cổ phiếu và giới hạn gọi API.
- [ ] Cho phép chọn chế độ thời tiết hoặc chứng khoán; đặt quy tắc LED phù hợp với giá cổ phiếu.
- [ ] Bổ sung cấu hình API key, tài liệu và kiểm thử cho chế độ mới.
