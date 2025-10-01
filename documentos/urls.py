from django.urls import path, include 
from .views import DigitalizarDocumento

urlpatterns = [
    path('Digitaliar_Documentos/', DigitalizarDocumento.as_view(), name="Digitalizar_Documentos")
]
