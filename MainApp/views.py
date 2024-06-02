from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def loginAndRegister(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        # Check if the request is for registration or login
        if 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('index')  # Redirect to home page after registration
        elif 'login' in request.POST:
            username_or_email = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('login_succes')  # Redirect to home page after login
            else:
                # Handle invalid login credentials
                # You can customize this based on your needs, like displaying error messages
                pass

    return render(request, 'MainApp/loginAndRegister.html', {'register_form': register_form})

def login_succes(request):
    return render(request, 'MainApp/login_succes.html')

def index(request):
    return render(request, 'MainApp/index.html')

def explore(request):
    return render(request, 'MainApp/explore.html')

@login_required
def profil(request):
    return render(request, 'MainApp/profil.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the desired page after logout
