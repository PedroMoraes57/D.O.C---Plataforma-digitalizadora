from django.contrib import admin
from usuarios.models import Usuarios
from documentos.models import Documentos

admin.site.register(Usuarios)
admin.site.register(Documentos)