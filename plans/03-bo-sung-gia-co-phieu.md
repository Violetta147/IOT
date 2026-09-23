# Cập nhật 3 — Bổ sung giá cổ phiếu

## Mục tiêu

Cho phép chọn theo dõi thời tiết hoặc giá một mã cổ phiếu. Raspberry Pi vẫn là client gọi API và điều khiển LED.

## Thực hiện

1. Chọn API chứng khoán có dữ liệu và hạn mức phù hợp; ghi rõ cách tạo API key và độ trễ dữ liệu.
2. Thêm cấu hình key riêng và chức năng lấy giá theo mã cổ phiếu. Không lưu key thật trong Git hoặc in key trong thông báo lỗi.
3. Thêm cách chọn chế độ và nhập mã cổ phiếu. Giữ chức năng thời tiết hiện có hoạt động như trước.
4. Đặt quy tắc LED riêng cho giá cổ phiếu, chẳng hạn giá thấp hơn ngưỡng thì bật; cho phép cấu hình ngưỡng và khoảng cập nhật theo giới hạn của API đã chọn.
5. Cập nhật README và kiểm thử với phản hồi API giả: lấy giá, so sánh ngưỡng, chuyển chế độ và xử lý lỗi gọi API.

## Hoàn thành khi

- Người dùng có thể chọn chế độ, xem giá cổ phiếu và trạng thái LED tương ứng.
- Chương trình không vượt hạn mức API trong cách dùng thông thường; thời tiết vẫn chạy đúng.
- Bài kiểm thử đạt và đã thử với API key thật; kiểm tra LED trên Raspberry Pi khi có thiết bị.
