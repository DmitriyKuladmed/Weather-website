
from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')

def page(request):
    return render(request, 'weather/page.html')
