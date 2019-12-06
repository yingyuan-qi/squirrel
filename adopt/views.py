from django.shortcuts import render
from django.http import HttpResponse

from .models import Sighting

def all_squirrels(request):
    squirrels = Sighting.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'adopt/sighting.html', context)
