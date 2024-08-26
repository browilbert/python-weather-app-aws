from flask import Flask, render_template, request
import requests

app = Flask(__name__)

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    api_key = 'fb51538df9adeecc7c74098df8020eff'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == 200:
        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
        return render_template('weather.html', weather=weather)
    else:
        return render_template('error.html', message=weather_data['message'])

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
