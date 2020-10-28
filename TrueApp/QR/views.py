from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import TrueApp

def index(request, app_name):


    trueapp = get_object_or_404(TrueApp, app_name = app_name)

    context = {
        'trueapp': trueapp,
        }

    return render(request, 'QR/index.html', context)