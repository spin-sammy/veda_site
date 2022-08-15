from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('<h1>Hello Ukrainians!</h1>')

def test(request):
    print(request)
    return HttpResponse('<h1>Test page!</h1>')
