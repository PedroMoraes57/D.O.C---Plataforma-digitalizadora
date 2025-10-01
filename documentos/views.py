from django.shortcuts import render, redirect
from .models import Documento
from .forms import Formulario1_Documentos
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class DigitalizarDocumento(CreateView):
    model = Documento
    fields = ['nome', 'arquivo']
    template_name = 'documentos/DigitalizarDocumentos.html'
    success_url = reverse_lazy('Digitalizar_Documentos')