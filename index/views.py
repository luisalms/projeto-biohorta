from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Hello, World!")

def luisa(request):
    return HttpResponse("Hello, luisa! Deu certo!!")

def david(request):
    return HttpResponse("hello, david!")