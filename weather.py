import requests


def get_weather(city, api_key):
    location_response = requests.get(
        "https://api.openweathermap.org/geo/1.0/direct",
        params={"q": city, "limit": 1, "appid": api_key},
        timeout=10,
    )
    location_response.raise_for_status()
    locations = location_response.json()
    if not locations:
        raise ValueError("Không tìm thấy thành phố.")

    location = locations[0]
    weather_response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "lat": location["lat"],
            "lon": location["lon"],
            "units": "metric",
            "appid": api_key,
        },
        timeout=10,
    )
    weather_response.raise_for_status()
    current = weather_response.json()["main"]

    return location["name"], current["temp"], current["humidity"]
