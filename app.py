import os

from weather import get_weather


def should_light_led(temperature, threshold):
    return temperature < threshold


def main():
    city = input("Nhập thành phố: ").strip()
    api_key = os.environ["OPENWEATHER_API_KEY"]
    threshold = float(os.getenv("TEMP_THRESHOLD_C", "30"))
    name, temperature, humidity = get_weather(city, api_key)

    print(f"{name}: {temperature:.1f} °C, độ ẩm {humidity}%")

    from gpiozero import LED

    led = LED(17)
    try:
        if should_light_led(temperature, threshold):
            led.on()
            state = "bật"
        else:
            led.off()
            state = "tắt"
        print(f"Ngưỡng {threshold:g} °C: LED {state}")
        input("Nhấn Enter để kết thúc...")
    finally:
        led.off()
        led.close()


if __name__ == "__main__":
    main()
