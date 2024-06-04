# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Beatmaker, Music

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'full_name', 'country', 'profile_picture')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('full_name', 'email', 'country')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

class BeatmakerAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_description')

class MusicAdmin(admin.ModelAdmin):
    list_display = ('beatmaker', 'title', 'price', 'uploaded_at')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Beatmaker, BeatmakerAdmin)
admin.site.register(Music, MusicAdmin)
