from django.shortcuts import render
from .models import Documento
from django.views.generic import CreateView
# Create your views here.

class DigitalizarDocumentos(CreateView):
    model = Documento
    template_name = 'DigitalizarDocumentos.html'
    fields = "__all__"

