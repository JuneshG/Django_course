from . import views
from django.urls import path

urls = [
    path('', views.home, name='home'),
]