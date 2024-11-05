from django import forms
from .models import Reserva, Aviso

from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['area', 'data', 'hora', 'bloco']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        area = cleaned_data.get("area")
        hora = cleaned_data.get("hora")
        bloco = cleaned_data.get("bloco")
        
        if area in ['churrasqueira', 'piscina'] and hora:
            self.add_error('hora', "Churrasqueira e Piscina são reservadas por dia, sem horário específico.")
        elif area == 'salao-de-festa' and not bloco:
            self.add_error('bloco', "Escolha o bloco ao reservar o salão de festas.")
        elif area in ['quadra', 'sala-de-jogos'] and not hora:
            self.add_error('hora', "Selecione um horário ao reservar a quadra ou sala de jogos.")
        
        return cleaned_data


class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ['titulo', 'texto']


from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }