from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def login(request):
    return render(request, 'galeria/login.html')