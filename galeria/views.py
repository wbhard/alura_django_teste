from django.shortcuts import render


def index(request):
    return render(request, 'galeria/cadastro-cliente.html')

def login(request):
    return render(request, 'galeria/login.html')

def produto(request):
    return render(request, 'galeria/cadastro-produto.html')
