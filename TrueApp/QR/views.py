from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

from .models import TrueApp

def index(request, app_name):

    trueapp = get_object_or_404(TrueApp, app_name = app_name)

    context = {
        'trueapp': trueapp,
        }

    return render(request, 'QR/index.html', context)

def list (request):

    trueapp_list = TrueApp.objects.all()

    url_list = []
    for app in trueapp_list:
        trueapp = {
            'name': app.app_name, 
            'url': request.build_absolute_uri(reverse('QR:index', args=(app.app_name, ))) 
        } 
        url_list.append(trueapp)

    
    context = {
        'trueapp_list': trueapp_list,
        'url_list': url_list,

    }

    return render(request, 'QR/list.html', context)