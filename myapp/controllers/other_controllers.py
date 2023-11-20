import os
import requests
from dotenv import load_dotenv
from flask import jsonify, request

load_dotenv()

# Home Route
def welcome():
    return '<h1 style="text-align: center; margin-top: 20px; color: purple;">Welcome to the Wanderlust Travel Planner API!</h1>'

# Route for Weather Information
def get_weather():
    location = request.args.get('location')

    api_key = os.environ.get('openweather_api_key')

    # Define the OpenWeatherMap API URL with the location and API key
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
        response = requests.get(weather_url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'location': location,
                'temperature': data['main']['temp'],
                'wind_speed': data['wind']['speed'],
                'humidity': data['main']['humidity'],
                'condition': data['weather'][0]['description'],
            }
            return jsonify(weather_data), 200

        else:
            return jsonify({'error': 'Weather data not found.'}), 404

    except Exception as e:
        return jsonify({'error': 'Something Went Wrong!'}), 500