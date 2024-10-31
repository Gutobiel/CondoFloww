from django import forms
from .models import Reserva, Aviso

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['area', 'data', 'horario']

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ['titulo', 'texto']
