# Thời tiết và đèn LED trên Raspberry Pi

Nhập tên thành phố, lấy nhiệt độ và độ ẩm từ OpenWeather bằng API key. LED ở GPIO17 bật khi nhiệt độ **dưới 30°C** (hoặc ngưỡng bạn đặt), và tắt khi nhiệt độ bằng hoặc cao hơn ngưỡng.

## Chuẩn bị

- Raspberry Pi có Internet, Python 3 và một API key [OpenWeather](https://home.openweathermap.org/api_keys).
- LED, điện trở hạn dòng 220–330 Ω và dây nối.
- Nối **GPIO17 (chân vật lý 11) → điện trở → chân dài LED**; chân ngắn LED → **GND (chân vật lý 6)**. Tắt nguồn Pi trước khi nối mạch.

## Cài đặt và chạy

Trên Raspberry Pi, trong thư mục dự án:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp config.example.sh config.sh
```

Mở `config.sh`, thay `YOUR_API_KEY` bằng key của bạn, rồi chạy:

```sh
. ./config.sh
python app.py
```

Nhập `Hanoi,VN` khi được hỏi. Chương trình in nhiệt độ (°C), độ ẩm (%) và trạng thái LED; nhấn Enter để tắt LED và kết thúc. Muốn đổi ngưỡng, sửa `TEMP_THRESHOLD_C` trong `config.sh`.

## Kiểm thử

```sh
python -m unittest discover -s tests -v
```

Bài kiểm thử dùng dữ liệu API và LED giả nên chạy được khi không có Raspberry Pi hoặc API key. Chưa chạy thử API thật và mạch LED vì môi trường hiện tại không có key hay thiết bị Pi.

## Liên hệ với bài tập

Mục 10, trang 125–127 của *Getting Started with Raspberry Pi* giới thiệu HTTP, thư viện `requests`, mã phản hồi và API key cho dịch vụ thời tiết. Chương trình này áp dụng luồng đó với [Geocoding API](https://openweathermap.org/api/geocoding-api) để đổi tên thành phố thành tọa độ, rồi [Current Weather API](https://openweathermap.org/api/current) để lấy `main.temp` và `main.humidity` từ JSON. Ví dụ trong sách dùng Weather Underground; ứng dụng này dùng OpenWeather.
