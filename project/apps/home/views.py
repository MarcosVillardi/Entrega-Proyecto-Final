from django.shortcuts import render, redirect
from . import forms

def base(request):
    return render(request, 'home/base.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:base')
    else:
        form = forms.ClienteForm()
        context = {'form': form}
    return render(request, 'home/crear_cliente.html',context)

def registrar_habitacion(request):
    if request.method == 'POST':
        form = forms.ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:base')
    else:
        form = forms.ReservaForm()
        context = {'form': form}
    return render(request, 'home/registrar_habitacion.html',context)

def registrar_garaje(request):
    if request.method == 'POST':
        form = forms.GarajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:base')
    else:
        form = forms.GarajeForm()
        context = {'form': form}
    return render(request, 'home/registrar_garaje.html',context)