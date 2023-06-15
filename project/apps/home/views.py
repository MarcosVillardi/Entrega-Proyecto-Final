from django.shortcuts import render
from . import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
    return render(request, 'home/index.html')

def info(request):
    return render(request, 'home/about.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home/index.html',)
            else:
                return render(request, 'home/login.html', {'form': form})
        else:
            return render(request, 'home/login.html', {'form': form})
    form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def register_request(request):
      if request.method == 'POST':
            form = forms.CustomUserCreationForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"home/index.html" ,)
      else:
           form = forms.CustomUserCreationForm()      
      return render(request,"home/register.html",{"form":form})
