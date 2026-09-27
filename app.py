import os
from gpiozero import LED
from weather import get_weather

def should_light_led(temperature, threshold):
    return temperature < threshold

def main():
    api_key = os.environ["OPENWEATHER_API_KEY"]
    threshold = float(os.getenv("TEMP_THRESHOLD_C", "30"))
    
    # Initialize the LED once outside the loop
    led = LED(17)
    
    try:
        # Loop continuously until the user exits
        while True:
            city = input("Nhập thành phố (hoặc nhập 'q' để thoát): ").strip()
            
            if city.lower() == 'q':
                break
                
            try:
                name, temperature, humidity = get_weather(city, api_key)
            except ValueError as error:
                print(f"Lỗi: {error}")
                continue  # Skip to the next iteration instead of exiting

            print(f"{name}: {temperature:.1f} °C, độ ẩm {humidity}%")

            if should_light_led(temperature, threshold):
                led.on()
                state = "bật"
            else:
                led.off()
                state = "tắt"
                
            print(f"Ngưỡng {threshold:g} °C: LED {state}")
            print("-" * 30) # Visual separator for the next input
            
    finally:
        # Safely turn off and release the pin when the program ends
        led.off()
        led.close()

if __name__ == "__main__":
    main()
