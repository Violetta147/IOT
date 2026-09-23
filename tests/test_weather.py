import unittest
from unittest.mock import Mock, patch

import requests

from weather import get_weather


class GetWeatherTests(unittest.TestCase):
    @patch("weather.requests.get")
    def test_fetches_weather_for_city(self, get):
        get.side_effect = [
            Mock(json=Mock(return_value=[{"name": "Hanoi", "lat": 21.0, "lon": 105.8}])),
            Mock(json=Mock(return_value={"main": {"temp": 28.5, "humidity": 72}})),
        ]

        self.assertEqual(get_weather("Hanoi,VN", "test-key"), ("Hanoi", 28.5, 72))
        self.assertEqual(get.call_count, 2)
        self.assertEqual(get.call_args_list[0].kwargs["params"]["q"], "Hanoi,VN")
        self.assertEqual(get.call_args_list[1].kwargs["params"]["units"], "metric")

    @patch("weather.requests.get")
    def test_unknown_city(self, get):
        get.return_value.json.return_value = []

        with self.assertRaisesRegex(ValueError, "Không tìm thấy thành phố"):
            get_weather("Unknown", "test-key")

    @patch("weather.requests.get")
    def test_unauthorized_does_not_reveal_key(self, get):
        response = Mock(status_code=401)
        response.raise_for_status.side_effect = requests.HTTPError(
            "401 for URL with secret-key", response=response
        )
        get.return_value = response

        with self.assertRaises(ValueError) as caught:
            get_weather("Hanoi,VN", "secret-key")

        self.assertIn("API key", str(caught.exception))
        self.assertNotIn("secret-key", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
