from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.urls import reverse


def index(request):
    return render(request, 'MainApp/index.html')

def explore(request):
    return render(request, 'MainApp/explore.html')



def login(request): #login + register
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))  
    else:
        form = CustomUserCreationForm()
    return render(request, 'MainApp/login.html', {'form': form})
