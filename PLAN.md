# Kế hoạch: Lấy dữ liệu thời tiết từ Internet

## Mục tiêu

Viết chương trình Python trên Raspberry Pi: nhập tên thành phố, dùng API key lấy nhiệt độ và độ ẩm từ web server, hiển thị kết quả và điều khiển đèn LED theo ngưỡng nhiệt độ.

## Các bước

1. Đối chiếu mục 10, trang 125–127 của *Getting Started with Raspberry Pi*; chọn API thời tiết và cách nối LED với GPIO.
2. Viết chương trình đọc API key từ biến môi trường, gọi API theo thành phố và xử lý dữ liệu JSON.
3. Hiển thị nhiệt độ, độ ẩm; bật hoặc tắt LED theo ngưỡng cấu hình. Xử lý lỗi mạng, API key và tên thành phố.
4. Viết hướng dẫn cài đặt, chạy chương trình và nối mạch. Kiểm thử phần lấy dữ liệu, logic LED và chạy thử trên Raspberry Pi.

## Kết quả cần có

Mã nguồn, tệp khai báo thư viện, mẫu cấu hình API key, hướng dẫn sử dụng và bài kiểm thử. API key thật không được đưa vào Git.

Tham khảo: [repo ví dụ](https://github.com/dothang13/lthtn2026_weather).
