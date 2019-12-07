from django.shortcuts import render
from django.http import HttpResponse

from .models import Sightings

def display_map(request):
    context = {
            'map':map,
    }
    return render(request, 'adopt/map.html', context)

def all_squirrels(request):
    squirrels = Sightings.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'adopt/sightings.html', context)

