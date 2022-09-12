import requests
from django.shortcuts import render

def index(request):
    appid = '9c6a500132fd69ee6ab45142b7de969b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Minsk'
    res = requests.get(url.format(city))

    print(res.text)

    return render(request, 'weather/index.html')


def page(request):
    return render(request, 'weather/page.html')
