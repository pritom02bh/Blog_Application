from django.shortcuts import render
from django.hppt import HttpResponse


def home(request):
    return Httpresponse('<h1>Blog Home</h1>')
