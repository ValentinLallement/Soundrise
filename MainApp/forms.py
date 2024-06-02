from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'country', 'password1', 'password2']