from django.db import models

class Perfil(models.Model):
    objects = None
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField(null=True, blank=True)  # Opcional

    def _str_(self):
        return self.nome


class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    duracao = models.DurationField(help_text="Duração da música (HH:MM:SS)")
    genero = models.CharField(max_length=50, blank=True, null=True)
    data_lancamento = models.DateField(blank=True, null=True)

    def _str_(self):
        return f"{self.titulo} - {self.artista}"


class Playlist(models.Model):
    usuario = models.CharField(max_length=100)  # Modificado para um campo CharField
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    musicas = models.ManyToManyField(Musica, related_name='playlists')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.nome} ({self.usuario})"


class Biblioteca(models.Model):
    usuario = models.CharField(max_length=100)  # Modificado para um campo CharField
    musicas_favoritas = models.ManyToManyField(Musica, related_name='bibliotecas', blank=True)
    playlists_salvas = models.ManyToManyField(Playlist, related_name='bibliotecas', blank=True)

    def _str_(self):
        return f"Biblioteca de {self.usuario}"