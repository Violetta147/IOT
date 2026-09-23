# Bước 3 — Hiển thị và điều khiển LED

## Cần làm

1. Tạo luồng chạy chính: hỏi tên thành phố, gọi phần lấy thời tiết ở bước 2 và hiển thị tên địa điểm, nhiệt độ (°C), độ ẩm (%).
2. Đọc ngưỡng từ `TEMP_THRESHOLD_C` (mặc định 30°C); kiểm tra cấu hình là số hợp lệ. Dùng `gpiozero.LED` để điều khiển chân GPIO đã chốt ở bước 1.
3. Áp dụng một quy tắc rõ ràng: **nhiệt độ < ngưỡng: bật LED; nhiệt độ ≥ ngưỡng: tắt LED**. Hiển thị ngưỡng và trạng thái LED để dễ kiểm tra.
4. Nếu không lấy được dữ liệu mới, không dùng giá trị cũ để quyết định; báo lỗi và đưa LED về trạng thái tắt. Tắt LED và giải phóng GPIO khi chương trình kết thúc.
5. Tách phép so sánh nhiệt độ khỏi lệnh GPIO để có thể kiểm thử logic trên máy không có Raspberry Pi.

## Hoàn thành khi

- Hai giá trị ở hai phía ngưỡng tạo đúng hai trạng thái LED; đúng bằng ngưỡng thì LED tắt.
- Khi API lỗi hoặc người dùng thoát, LED tắt và chương trình kết thúc gọn.

Nguồn kỹ thuật: [GPIO Zero](https://gpiozero.readthedocs.io/en/latest/).
