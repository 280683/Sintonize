from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('playlist/', views.playlist, name='playlist'),
    path('adicionar_perfil/', views.adicionar_perfil, name='adicionar_perfil'),
]