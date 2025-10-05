from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения коробков")

def series(request):
    return HttpResponse("<h1>Серии спичечных коробков</h1>")