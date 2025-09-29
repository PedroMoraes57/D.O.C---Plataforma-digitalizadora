from django.db import models

class Documentos (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=20, null=False, blank=False) 
    setor = models.CharField(max_length=25, null=False, blank=False)
    data_publicacao = models.DateTimeField(max_length=25, null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.nome