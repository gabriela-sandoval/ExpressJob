from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "ExpressJobApp/inicio.html")

def login(request):
    return render(request, "ExpressJobApp/login.html")

def registro(request):
    return render(request, "ExpressJobApp/registro.html")

def principal(request):
    return render(request, "ExpressJobApp/principal.html")