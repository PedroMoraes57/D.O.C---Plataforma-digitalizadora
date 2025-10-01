from django import forms
from .models import Documento

class Formulario1_Documentos(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['arquivo', 'nome']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Insira o nome do seu documento...'})
        }

