from rest_framework import serializers
from .models import Usuario
from django.forms import ModelForm

class UsuarioSerializer(ModelForm):
  class Meta:
    model = Usuario
    fields = ('Nome', 'Idade', 'Apelido', 'Cargo')