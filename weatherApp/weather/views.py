import requests
from django.shortcuts import render

def index(request):
    appid = '9c6a500132fd69ee6ab45142b7de969b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'wind': res['wind']['speed']
    }

    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)


def page(request):
    return render(request, 'weather/page.html')
