import requests
import os

def get_weather(query):
    api_key = os.getenv("WEATHER_API_KEY")
    # Clean the query: remove question marks and extra spaces
    city = query.replace("?", "").strip()
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"The current temperature in {city} is {temp}°C with {desc}."
        else:
            return f"Error: {data.get('message', 'City not found')}"
    except Exception as e:
        return f"Connection error: {e}"