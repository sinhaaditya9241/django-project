from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a success page or login page
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')