from django.shortcuts import render, redirect
from . import forms

def index(request):
    return render(request, 'home/index.html')

def info(request):
    return render(request, 'home/about.html')