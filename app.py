from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '77e64e886c3fd4391a750c7172bfdc13'

@app.route('/', methods=['GET', 'POST'])


def index():
    weather_data = None
    forecast_data = None
    error_message = None
   
    if request.method == 'POST':
        city = request.form['city']
        current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        current_weather_response = requests.get(current_weather_url)
        weather_data = current_weather_response.json()
        

        if weather_data.get('cod') != 200:
            error_message = weather_data.get('message', 'try again please!')
            weather_data = None
        else:
            forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            # بررسی وضعیت پاسخ برای پیش‌بینی آب‌وهوا
            if forecast_data.get('cod') != '200':
                forecast_data = None
    
    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
