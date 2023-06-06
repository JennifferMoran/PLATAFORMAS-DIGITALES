from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def bienvenida (request):
    print ('Hola')
    return HttpResponse ('<!Doctype HTLM><html><head><title>APP</title></head><body><p>Hola Mundo desde Django</p></body>')

def hola(request,nombre):
    mensaje ={'nombre':nombre. upper()}
    return HttpResponse (mensaje)
