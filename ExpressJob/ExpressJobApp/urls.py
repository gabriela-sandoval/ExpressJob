from django.urls import path
from ExpressJobApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('login', views.login, name="Login"),
    path('registro', views.registro, name="Registro"),
    path('principal', views.principal, name="Principal"),
]