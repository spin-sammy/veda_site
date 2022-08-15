from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    print(request)
    return HttpResponse('<h1>Hello Games</h1>')

def test_game(request):
    print(request)
    return HttpResponse('<h1>Test games page!</h1>')