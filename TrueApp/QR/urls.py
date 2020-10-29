""" QR URLS """

from django.urls import path, include
from . import views

app_name = 'QR'
urlpatterns = [
    path('<str:app_name>/', views.index, name='index'),
    path('app/list/', views.list, name='list'),
]
