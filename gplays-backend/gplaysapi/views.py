from django.shortcuts import redirect, render




def home(request):
    data = {}
    return render(request, 'home.html', data)
# Create your views here.
