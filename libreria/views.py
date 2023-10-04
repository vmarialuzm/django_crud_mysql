from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido Develoteca")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


