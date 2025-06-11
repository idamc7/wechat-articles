import httpx
from typing import Dict, Any

class WeatherService:
    """
    Service to interact with the QWeather API.
    """
    def __init__(self, api_key: str, base_url: str):
        if not api_key:
            raise ValueError("QWeather API key is required.")
        self.api_key = api_key
        self.base_url = base_url

    def get_daily_weather(self, location_id: str) -> Dict[str, Any]:
        """
        Fetches the 3-day weather forecast for a specific location.
        """
        params = {"location": location_id}
        headers = {'X-QW-Api-Key': self.api_key}
        try:
            with httpx.Client() as client:
                response = client.get(f"{self.base_url}/3d", params=params, headers=headers)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            # Add more specific error handling based on QWeather's error codes
            print(f"Error fetching weather data: {e}")
            return {}
        
if __name__ == "__main__":
    weather_service = WeatherService(api_key="your_api_key", base_url="https://your_host/v7/weather");
    print(weather_service.get_daily_weather("your_location_id"))