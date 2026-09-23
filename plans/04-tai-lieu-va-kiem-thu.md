# Bước 4 — Tài liệu và kiểm thử

## Cần làm

1. Viết `README.md`: yêu cầu phần cứng/phần mềm, sơ đồ nối LED, cách cài thư viện, tạo API key, đặt biến môi trường và chạy chương trình với một thành phố mẫu.
2. Tạo tệp mẫu cấu hình không chứa key thật và `.gitignore` để tránh commit key, môi trường ảo hoặc tệp tạm.
3. Viết kiểm thử tự động với dữ liệu API giả: kết quả hợp lệ và thành phố không tồn tại. Không gọi API thật trong các bài kiểm thử này.
4. Kiểm thử logic LED với nhiệt độ dưới, bằng và trên ngưỡng; dùng GPIO giả để kiểm tra lệnh bật/tắt.
5. Chạy toàn bộ kiểm thử. Sau đó dùng API key thật thử một thành phố và, khi có Raspberry Pi, kiểm tra LED cùng điện trở trên mạch thật. Ghi lại kết quả và mọi giới hạn chưa kiểm tra được.

## Hoàn thành khi

- Người khác có thể làm theo `README.md` để cài đặt và chạy chương trình mà không cần xem mã nguồn.
- Kiểm thử tự động chạy thành công; thử API và LED trên thiết bị thật khi có API key và Raspberry Pi.
- Git không chứa API key thật.
