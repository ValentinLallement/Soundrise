from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, ProfilePictureForm
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
def profile(request):
    user = request.user
    return render(request, 'MainApp/profile.html', {'user': user})

def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=request.user)
    return render(request, 'upload_profile_picture.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the desired page after logout

def setting_view(request, page):
    print(page)
    return render(request, 'MainApp/parametre/parametre_activite_com.html')

