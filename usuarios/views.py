from django.shortcuts import render
from .models import Usuario
from django.views.generic import CreateView
# Create your views here.

def pagina_login(request):
    return render(request, 'usuarios/login.html')

class perfil(CreateView):
    model = Usuario
    template_name = 'usuarios/TemplatePerfil.html'
    fields = "__all__"

