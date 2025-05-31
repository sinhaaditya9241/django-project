from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return render(request, 'hello.html', {'name': 'tom '})

def add(request):
    return render(request, 'result.html')