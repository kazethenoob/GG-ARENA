from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('register')),  # Redirect root URL to register
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]