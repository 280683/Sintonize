from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Perfil
from .serializer import PerfilSerializer

class PerfilListCreateView(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PerfilRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

def index(request):
    return render(request, 'index.html')

def biblioteca(request):
    return render(request, 'biblioteca.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login_view(request):
    return render(request, 'login.html')

def perfil(request):
    perfis = Perfil.objects.filter(usuario=request.user)
    return render(request, 'perfil.html', {'perfis': perfis})

def playlist(request):
    return render(request, 'playlist.html')

from django.shortcuts import render, redirect
from .models import Perfil

def adicionar_perfil(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:  # Se o nome não for vazio
            Perfil.objects.create(nome=nome, usuario=request.user)
            return redirect('perfil')
    return render(request, 'adicionar_perfil.html')

def salvar(request):
    nome = request.POST.get("nome")
    Perfil.objects.create(nome=nome, usuario=request.user)
    perfis = Perfil.objects.all()
    return render(request, "perfil.html", {"perfis": perfis})

def editar_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    if request.method == 'POST':
        perfil.nome = request.POST.get('nome')
        perfil.data_nascimento = request.POST.get('data_nascimento')
        perfil.save()
        return redirect('perfil')
    return render(request, 'editar_perfil.html', {'perfil': perfil})

def update(request, id):
    vnome = request.POST.get("nome")
    perfil = Perfil.objects.get(id=id)
    perfil.nome = vnome
    perfil.save()
    return redirect('perfil')

def confirmar_exclusao(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfil')
    return render(request, 'confirmar_exclusao.html', {'perfil': perfil})

def excluir_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfil')
    return redirect('confirmar_exclusao', perfil_id=perfil_id)


