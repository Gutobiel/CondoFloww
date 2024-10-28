from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def avisos(request):
    return render(request, "core/avisos.html")

def registros(request):
    return render(request, "core/registros.html")

def cobranca(request):
    return render(request, "core/cobranca.html")

def reuniao(request):
    return render(request, "core/reuniao.html")

def reserva(request):
    return render(request, "core/reserva.html")

def configuracoes(request):
    return render(request, "core/configuracoes.html")

def login(request):
    return render(request, "core/login.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'core/home.html')