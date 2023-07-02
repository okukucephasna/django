from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid form data."
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('login')
