import requests

# Weather using Open-Meteo (no API key required)
def get_weather(city: str):
    locations = {
        "New York": [40.7128, -74.0060],
        "London": [51.5074, -0.1278],
        "Paris": [48.8566, 2.3522],
        "Tokyo": [35.6762, 139.6503]
    }
    lat, lon = locations.get(city, [40.7128, -74.0060])
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        data = requests.get(url).json()
        temp = data['current_weather']['temperature']
        wind = data['current_weather']['windspeed']
        return f"The current temperature in {city} is {temp}°C with wind speed {wind} km/h."
    except:
        return "Sorry, I couldn't fetch the weather."

# Placeholder news function
def get_news():
    headlines = [
        "News headlines are not available right now.",
        "You can integrate NewsAPI.org or Mediastack later."
    ]
    return "\n".join(headlines)

