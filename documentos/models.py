from django.db import models
from usuarios.models import Usuarios
class Documentos (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=20, null=False, blank=False) 
    setor = models.CharField(max_length=25, null=False, blank=False)
    assunto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(max_length=25, null=False, blank=False, auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    # Campos extra extraídos via OCR/IA
    prazo = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome