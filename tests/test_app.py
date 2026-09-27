import unittest
from unittest.mock import patch

from app import main, should_light_led


class AppTests(unittest.TestCase):
    def test_temperature_threshold(self):
        self.assertTrue(should_light_led(29.9, 30))
        self.assertFalse(should_light_led(30, 30))
        self.assertFalse(should_light_led(30.1, 30))

    @patch.dict("os.environ", {"OPENWEATHER_API_KEY": "test-key", "TEMP_THRESHOLD_C": "30"})
    @patch("app.get_weather", return_value=("Hanoi", 28.5, 72))
    @patch("builtins.input", side_effect=["Hanoi,VN", "q"])
    @patch("app.LED")
    def test_main_turns_led_on_and_cleans_up(self, led_type, user_input, get_weather):
        with patch("builtins.print"):
            main()

        led = led_type.return_value
        get_weather.assert_called_once_with("Hanoi,VN", "test-key")
        led.on.assert_called_once()
        led.off.assert_called_once()
        led.close.assert_called_once()

    @patch.dict("os.environ", {"OPENWEATHER_API_KEY": "test-key", "TEMP_THRESHOLD_C": "30"})
    @patch("app.get_weather", return_value=("Hanoi", 30, 72))
    @patch("builtins.input", side_effect=["Hanoi,VN", "q"])
    @patch("app.LED")
    def test_main_keeps_led_off_at_threshold(self, led_type, user_input, get_weather):
        with patch("builtins.print"):
            main()

        led = led_type.return_value
        led.on.assert_not_called()
        self.assertEqual(led.off.call_count, 2)
        led.close.assert_called_once()

    @patch.dict("os.environ", {"OPENWEATHER_API_KEY": "test-key"})
    @patch("app.get_weather", side_effect=ValueError("API key không hợp lệ."))
    @patch("builtins.input", side_effect=["Hanoi,VN", "q"])
    @patch("app.LED")
    def test_main_shows_api_error(self, led_type, user_input, get_weather):
        with patch("builtins.print") as output:
            main()

        output.assert_called_once_with("Lỗi: API key không hợp lệ.")
        led_type.return_value.close.assert_called_once()

    @patch.dict("os.environ", {"OPENWEATHER_API_KEY": "test-key", "TEMP_THRESHOLD_C": "30"})
    @patch("app.get_weather", side_effect=[("Hanoi", 28.5, 72), ("Da Nang", 31, 65)])
    @patch("builtins.input", side_effect=["Hanoi,VN", "Da Nang,VN", "q"])
    @patch("app.LED")
    def test_main_accepts_another_city(self, led_type, user_input, get_weather):
        with patch("builtins.print"):
            main()

        self.assertEqual(get_weather.call_count, 2)
        led = led_type.return_value
        led.on.assert_called_once()
        self.assertEqual(led.off.call_count, 2)
        led.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
