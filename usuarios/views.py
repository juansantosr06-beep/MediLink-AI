from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return render(request, 'usuarios/registro.html')

#@login_required  #aqui para ver el diseño tuve que comentar el arroba para evitar el inicio de secion
def dashboard_view(request):
    return render(request, 'usuarios/dashboard.html')
