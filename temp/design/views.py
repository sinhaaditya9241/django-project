from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def add(request):
    return HttpResponse("Hello, world. You're at the add page.")