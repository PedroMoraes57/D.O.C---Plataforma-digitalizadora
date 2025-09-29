from django.db import models

class Usuarios (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=20, null=False, blank=False, unique=True) 
    telefone = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.nome