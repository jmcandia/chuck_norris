from django import forms
from django.forms import ModelForm

from facts.models import Fact


class FactForm(ModelForm):
    class Meta:
        model = Fact
        fields = ['fact']


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=250, min_length=3, label='Ingrese su nombre de usuario')
    password = forms.CharField(min_length=8, max_length=16,
                               label='Ingrese su contraseña', widget=forms.PasswordInput())
