from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def biblioteca(request):
    return render(request, 'biblioteca.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login_view(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')

def playlist(request):
    return render(request, 'playlist.html')

def adicionar_perfil(request):
    return render(request, 'adicionar_perfil.html')