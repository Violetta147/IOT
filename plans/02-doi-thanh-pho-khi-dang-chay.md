# Cập nhật 2 — Đổi thành phố khi đang chạy

## Mục tiêu

Người dùng đổi thành phố từ terminal mà không cần khởi động lại chương trình ở cập nhật 1.

## Thực hiện

1. Thêm lệnh `city <tên thành phố>` và `quit` trong lúc chương trình chờ lần cập nhật tiếp theo.
2. Khi đổi thành phố, gọi Geocoding API cho tên mới. Nếu tìm thấy, lưu tọa độ mới, lấy thời tiết ngay và bắt đầu lại chu kỳ chờ.
3. Nếu không tìm thấy thành phố, giữ thành phố cũ và báo ngắn gọn để người dùng nhập lại.
4. Hiển thị tên thành phố hiện tại cùng nhiệt độ, độ ẩm và trạng thái LED sau mỗi lần cập nhật.
5. Bổ sung hướng dẫn nhập lệnh và kiểm thử việc đổi thành phố, giữ thành phố cũ khi nhập sai, cùng thời điểm cập nhật kế tiếp.

## Hoàn thành khi

- Đổi thành phố có hiệu lực ngay, không phải chạy lại chương trình.
- Geocoding API chỉ được gọi khi chọn thành phố ban đầu hoặc khi đổi thành phố.
- Có thể gõ `quit` để tắt LED và thoát gọn.
