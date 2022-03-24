from django.db import models

# Create your models here.

class Usuario(models.Model):
  Nome = models.CharField(max_length=50)
  Idade = models.IntegerField()
  Apelido = models.CharField(max_length=30)
  Cargo = models.CharField(max_length=30)