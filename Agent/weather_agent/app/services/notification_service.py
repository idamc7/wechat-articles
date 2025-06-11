import httpx

class NotificationService:
    """
    Service for sending push notifications via Bark.
    """
    def __init__(self):
        pass

    def send_notification(self, key: str, title: str, body: str, sound: str = "chime"):
        """
        Sends a notification to all configured devices.
        """
        url = f"https://api.day.app/{key}"
        payload = {
            "title": title,
            "body": body,
            "sound": sound,
            "group": "weather",
            "icon": "https://raw.githubusercontent.com/QWeather/QWeather-Icons/master/icons/100.png" # Sunny icon
        }
        try:
            httpx.post(url, json=payload)
        except httpx.RequestError as e:
            print(f"Error sending notification to {key}: {e}")

if __name__ == "__main__":
    notification_service = NotificationService()
    notification_service.send_notification("your_key", "测试", "测试内容")