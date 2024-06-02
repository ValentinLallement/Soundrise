from django.urls import path
from . import views

urlpatterns = [
    path('loginAndRegister/', views.loginAndRegister, name='loginAndRegister'),
    path('login_succes/', views.login_succes, name='login_succes'),
    path('explore/', views.explore, name='explore'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]