import yaml
import schedule
import time
from app.services.weather_service import WeatherService
from app.services.notification_service import NotificationService
from app.agents.weather_agent import WeatherAgent

def load_config():
    with open('config/config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def run_job():
    config = load_config()
    
    weather_service = WeatherService(api_key=config['qweather_api_key'], base_url=config['qweather_base_url'])
    notification_service = NotificationService()
    weather_agent = WeatherAgent(api_key=config['deepseek_api_key'])

    for user in config['users']:
        print(f"Fetching weather for {user['name']} in {user['city']}...")
        weather_data = weather_service.get_daily_weather(user['location_id'])
        
        if weather_data and weather_data.get('code') == '200':
            report = weather_agent.generate_weather_report(
                user_name=user['name'],
                city=user['city'],
                weather_data=weather_data
            )
            print(f"Generated report for {user['name']}:\n{report}")
            
            # Send notification to all devices for each user's report
            notification_service.send_notification(
                key=user['bark_key'],
                title=f"{user['city']} 天气提醒 🌤️",
                body=report
            )
            print(f"Notification sent for {user['name']}.")
        else:
            print(f"Could not retrieve weather for {user['name']}. Response: {weather_data}")

def main():
    config = load_config()
    cron_time = f"{config['cron_hour']:02d}:{config['cron_minute']:02d}"
    
    print(f"Scheduling job to run daily at {cron_time}.")
    schedule.every().day.at(cron_time).do(run_job)
    
    # Run once immediately for testing if needed
    run_job()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()