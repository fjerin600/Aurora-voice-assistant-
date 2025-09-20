import requests
import os
import json

# Load API keys from settings.json if it exists
API_KEYS = {"weather_api_key": "", "news_api_key": ""}
if os.path.exists("settings.json"):
    with open("settings.json") as f:
        API_KEYS.update(json.load(f))

def get_weather(city: str):
    key = API_KEYS.get("weather_api_key")
    if not key:
        return "Weather API key not set in settings.json."
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {desc}."
    except:
        return "Sorry, I couldn't fetch the weather."

def get_news():
    key = API_KEYS.get("news_api_key")
    if not key:
        return "News API key not set in settings.json."
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}"
    try:
        data = requests.get(url).json()
        headlines = [article['title'] for article in data['articles'][:5]]
        return "Here are the top news headlines:\n" + "\n".join(headlines)
    except:
        return "Sorry, I couldn't fetch the news."
