from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('playlist/', views.playlist, name='playlist'),

    path('api/perfil/', views.perfil, name='perfil'),
    path('api/perfil/', views.PerfilListCreateView.as_view(), name='perfil-list-create'),
    path('salvar/', views.salvar, name='salvar'),
    path('adicionar/', views.adicionar_perfil, name='adicionar_perfil'),
    path('editar/<int:perfil_id>/', views.editar_perfil, name='editar_perfil'),
    path('excluir/<int:perfil_id>/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('excluir/<int:perfil_id>/', views.excluir_perfil, name='excluir_perfil'),
]
