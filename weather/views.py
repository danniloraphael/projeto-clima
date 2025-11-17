import requests
from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timezone, timedelta

def index(request):
    weather = None
    error_msg = None

    if request.method == 'POST':
        city = request.POST.get('city')

        api_key = settings.OPENWEATHER_API_KEY
        
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            timezone_offset_seconds = data['timezone']
            city_timedelta = timedelta(seconds=timezone_offset_seconds)
            city_tz = timezone(city_timedelta)
            local_time = datetime.now(city_tz)
            utc_string = city_tz.tzname(None)

            wind_speed_mps = data['wind']['speed']
            wind_speed_kph = round(wind_speed_mps * 3.6, 2)
            
            weather = {
                'city_name': data['name'],
                'country': data['sys']['country'],
                'icon': data['weather'][0]['icon'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
                'humidity': data['main']['humidity'],
                'local_time': local_time.strftime('%H:%M'),
                'utc_offset': utc_string,
                'wind_speed': wind_speed_kph
            }
        else:
            error_msg = 'Cidade não encontrada'

    return render(
        request, 
        'weather/index.html', 
        {
            'weather': weather,
            'error_msg': error_msg
        }
    )
