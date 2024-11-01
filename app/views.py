from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def json_view(request):
    return HttpResponse("Hai.....")