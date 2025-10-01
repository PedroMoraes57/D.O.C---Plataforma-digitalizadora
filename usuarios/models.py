from django.db import models
from django_countries.fields import CountryField

## Esse modelo de usuário será corrigido, portanto, desconsidere o atual
class Usuarios (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    pais = CountryField(blank_label=("Selecione um país"))
    telefone = models.CharField(max_length=25, null=False, blank=False)
    foto_perfil = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome