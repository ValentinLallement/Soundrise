from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

class Beatmaker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='beatmaker_profile')
    profile_description = models.TextField(blank=True, null=True)
    # Other fields specific to beatmakers

class Music(models.Model):
    beatmaker = models.ForeignKey(Beatmaker, on_delete=models.CASCADE, related_name='music')
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='music/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Other fields as needed
