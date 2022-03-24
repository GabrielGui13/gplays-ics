from rest_framework import serializers
from .models import Usuario

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ('Nome', 'Idade', 'Apelido', 'Cargo')