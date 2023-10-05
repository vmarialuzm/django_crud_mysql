from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola Rafa")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    return render(request, 'libros/index.html')
