from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('json/', views.json_view, name='json_view'),
]


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def json_view(request):
    return HttpResponse("Hai.....")