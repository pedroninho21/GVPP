from django.shortcuts import render
from .models import *


def Home(request):

    context = {}

    if request.method == 'GET':
        services = Service.objects.all()
        used_cars = Used_Car.objects.all()

        
        
        context['services'] = services
        context['used_cars'] = used_cars

    return render(request, 'index.html', context)


def Contact(request):

    return render(request, 'contact-4.html')