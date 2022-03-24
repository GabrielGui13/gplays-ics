from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializer import NoteSerializer 

# class UsuarioViewSet(ModelViewSet):
#    serializer_class = NoteSerializer

def home(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'home.html', context)

def create(request):
    data={}
    return render(request, 'create.html', data)
