from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('polls/login.html', auth_views.LoginView.as_view(template_name="polls/login.html"), name='login')
]
