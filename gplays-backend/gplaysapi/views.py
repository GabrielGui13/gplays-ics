from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializer import UsuarioSerializer

def home(request):
    data = {}
    data['usuarios'] = Usuario.objects.all()
    return render(request, 'home.html', data)

def create(request):
    data = {}
    data['usuario'] = UsuarioSerializer(Usuario)
    return render(request, 'form.html', data)

def createindb(request):
    usuario = UsuarioSerializer(request.POST or None)
    if usuario.is_valid():
        usuario.save()
        return redirect('home')

def edit(request, id):
    data = {}
    data['editdata'] = Usuario.objects.get(id=id)
    data['usuario'] = UsuarioSerializer(instance=data['editdata'])
    return render(request, 'form.html', data)

def update(request, id):
    data = {}
    data['editdata'] = Usuario.objects.get(id=id)
    usuario = UsuarioSerializer(request.POST or None, instance=data['editdata'])
    if usuario.is_valid():
        usuario.save()
        return redirect('home')
