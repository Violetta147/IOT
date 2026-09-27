# Kế hoạch dự án

## Phiên bản hiện tại — luồng chính

- [x] Đối chiếu mục 10, trang 125–127 của *Getting Started with Raspberry Pi*.
- [x] Nhập thành phố, dùng API key lấy nhiệt độ và độ ẩm từ OpenWeather.
- [x] Hiển thị dữ liệu và bật/tắt LED theo ngưỡng nhiệt độ cấu hình được.
- [x] Cho nhập nhiều thành phố liên tiếp và thoát bằng `q`.
- [x] Viết hướng dẫn cài đặt, nối mạch và bảo vệ API key khỏi Git/log lỗi.
- [x] Chạy 8 kiểm thử tự động; thử API thật và GPIO giả trong Codespaces.
- [ ] Thử LED và GPIO trên Raspberry Pi thật.

## Các cập nhật tiếp theo (theo thứ tự)

1. [Cập nhật 1 — Tự làm mới thời tiết](plans/01-tu-dong-cap-nhat-thoi-tiet.md): lấy dữ liệu theo chu kỳ và cập nhật LED.
2. [Cập nhật 2 — Đổi thành phố khi đang chạy](plans/02-doi-thanh-pho-khi-dang-chay.md): đổi địa điểm ngay cả khi chương trình đang chờ lần cập nhật tự động tiếp theo.
3. [Cập nhật 3 — Bổ sung giá cổ phiếu](plans/03-bo-sung-gia-co-phieu.md): thêm chế độ dữ liệu chứng khoán và quy tắc LED riêng.
