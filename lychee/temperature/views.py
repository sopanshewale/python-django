from django.shortcuts import render
from django.http import HttpResponse
from temperature.Temperature import Temperature
import random

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("The Web Application is owned by Data Science Folks at Aegis")

def records(request):
    weather_1 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_2 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_3 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_4 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_list = [weather_1, weather_2, weather_3, weather_4]  
    context = {
        'temp':weather_list
    }

    return render(request, 'weather.html', context) 
   
