import requests


def get_json(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        if error.response is not None and error.response.status_code == 401:
            raise ValueError("API key OpenWeather không hợp lệ hoặc chưa được kích hoạt.") from None
        raise ValueError("Không thể lấy dữ liệu từ OpenWeather.") from None
    return response.json()


def get_weather(city, api_key):
    locations = get_json(
        "https://api.openweathermap.org/geo/1.0/direct",
        {"q": city, "limit": 1, "appid": api_key},
    )
    if not locations:
        raise ValueError("Không tìm thấy thành phố.")

    location = locations[0]
    weather = get_json(
        "https://api.openweathermap.org/data/2.5/weather",
        {
            "lat": location["lat"],
            "lon": location["lon"],
            "units": "metric",
            "appid": api_key,
        },
    )
    current = weather["main"]

    return location["name"], current["temp"], current["humidity"]
