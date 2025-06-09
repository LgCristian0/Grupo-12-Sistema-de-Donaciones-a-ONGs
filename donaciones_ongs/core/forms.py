from django import forms
from .models import ONG, Campaña, Donante, Donacion

class ONGForm(forms.ModelForm):
    class Meta:
        model = ONG
        fields = ['nombre', 'descripcion', 'direccion']

class CampañaForm(forms.ModelForm):
    class Meta:
        model = Campaña
        fields = ['ong', 'nombre', 'meta', 'fecha_inicio', 'fecha_fin']

class DonanteForm(forms.ModelForm):
    class Meta:
        model = Donante
        fields = ['nombre', 'email', 'telefono']

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['donante', 'campaña', 'monto','fecha' ]


