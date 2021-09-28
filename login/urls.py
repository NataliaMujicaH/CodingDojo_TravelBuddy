from django.urls import path, include
from . import views

#path ('ruta', views.metodo),
urlpatterns = [
    path('', views.registrar),
    path('registrar', views.registrar),
    path('inicio', views.inicio),
    path('registro', views.registro),
    path('logout', views.logout),
]