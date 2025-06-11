import httpx


WEATHER_ICON_MAP = {
    # 晴天
    100: "clear-day.png",
    150: "clear-day.png",
    # 多云
    101: "cloudy.png",  # 多云，通用
    151: "cloudy.png",
    # 少云
    102: "partly-cloudy-day.png",
    152: "partly-cloudy-day.png",
    # 晴间多云
    103: "partly-cloudy-day.png",
    153: "partly-cloudy-day.png",
    # 阴
    104: "overcast.png", # 阴天，通用
    # 阵雨
    300: "drizzle.png",  # 阵雨，用小雨图标
    350: "drizzle.png",
    # 强阵雨
    301: "extreme-rain.png", # 强阵雨，用极端降雨
    351: "extreme-rain.png",
    # 雷阵雨
    302: "thunderstorms-day.png",
    # 强雷阵雨
    303: "thunderstorms-day-extreme-rain.png", # 强雷阵雨，用雷阵雨带极端降雨
    # 雷阵雨伴有冰雹
    304: "hail.png", # 冰雹，直接用冰雹图标，或者考虑 thunderstorms-day-hail.png 如果有
    # 小雨
    305: "drizzle.png",
    # 中雨
    306: "rain.png",
    # 大雨
    307: "extreme-rain.png",
    # 极端降雨
    308: "extreme-rain.png",
    # 毛毛雨/细雨
    309: "drizzle.png",
    # 暴雨
    310: "extreme-rain.png",
    # 大暴雨
    311: "extreme-rain.png",
    # 特大暴雨
    312: "extreme-rain.png",
    # 冻雨
    313: "sleet.png",
    # 小到中雨
    314: "drizzle.png", # 介于小雨和中雨之间，仍用小雨或通用雨
    # 中到大雨
    315: "rain.png",
    # 大到暴雨
    316: "extreme-rain.png",
    # 暴雨到大暴雨
    317: "extreme-rain.png",
    # 大暴雨到特大暴雨
    318: "extreme-rain.png",
    # 雨
    399: "rain.png",
    # 小雪
    400: "snow.png",
    # 中雪
    401: "snow.png",
    # 大雪
    402: "extreme-snow.png", # 大雪用极端雪
    # 暴雪
    403: "extreme-snow.png",
    # 雨夹雪
    404: "sleet.png",
    # 雨雪天气 (泛指)
    405: "sleet.png",
    # 阵雨夹雪
    406: "sleet.png",
    456: "sleet.png",
    # 阵雪
    407: "snow.png",
    457: "snow.png",
    # 小到中雪
    408: "snow.png",
    # 中到大雪
    409: "snow.png",
    # 大到暴雪
    410: "extreme-snow.png",
    # 雪
    499: "snow.png",
    # 薄雾
    500: "mist.png",
    # 雾
    501: "fog.png",
    # 霾
    502: "haze.png",
    # 扬沙
    503: "dust-day.png", # 扬沙，用白天沙尘
    # 浮尘
    504: "dust-day.png", # 浮尘，用白天沙尘
    # 沙尘暴
    507: "dust-wind.png", # 沙尘暴，用沙尘带风
    # 强沙尘暴
    508: "dust-wind.png", # 强沙尘暴，同上
    # 浓雾
    509: "fog.png", # 浓雾，仍用雾
    # 强浓雾
    510: "fog.png",
    # 中度霾
    511: "haze.png",
    # 重度霾
    512: "haze.png",
    # 严重霾
    513: "haze.png",
    # 大雾
    514: "fog.png",
    # 特强浓雾
    515: "fog.png",
    # 热
    900: "sun-hot.png",
    # 冷
    901: "thermometer-colder.png",
    # 未知或不适用（例如，如果和风返回999）
    999: "not-available.png"
}

def get_weather_icon(hefeng_code: int) -> str:
    """
    根据和风天气预报的iconDay代码，返回对应的basmilius/weather-icons图标文件名。

    Args:
        hefeng_code (int): 和风天气预报的iconDay代码。

    Returns:
        str: 对应的weather-icons图标文件名，如果找不到则返回 'not-available.png'。
    """
    return WEATHER_ICON_MAP.get(hefeng_code, "not-available.png")

class NotificationService:
    """
    Service for sending push notifications via Bark.
    """
    def __init__(self):
        pass

    def send_notification(self, key: str, title: str, body: str, sound: str = "chime", hefeng_code: int = 100):
        """
        Sends a notification to all configured devices.
        """
        url = f"https://api.day.app/{key}"
        icon_url = "https://idamc7.github.io/assets/images/weather/"+get_weather_icon(hefeng_code)
        payload = {
            "title": title,
            "body": body,
            "sound": sound,
            "group": "weather",
            "icon": icon_url
        }
        try:
            httpx.post(url, json=payload, timeout=30)
        except httpx.RequestError as e:
            print(f"Error sending notification to {key}: {e}")

if __name__ == "__main__":
    notification_service = NotificationService()
    notification_service.send_notification("your_key", "测试", "测试内容")