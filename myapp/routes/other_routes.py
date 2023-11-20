from myapp import app
from myapp.controllers.other_controllers import welcome, get_weather

# Home Route
@app.route('/')
def home():
    return welcome()

# Route for Weather Information
@app.route('/weather', methods=['GET'])
def weather_get():
    return get_weather()