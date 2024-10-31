from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ReservaForm, AvisoForm
from .models import Reserva, Aviso
from django.views.decorators.http import require_POST

# Função para verificar se o usuário é administrador
def is_admin(user):
    return user.is_superuser

# View para criar uma reserva
@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('listar_reservas')  # Redireciona para a página de listagem de reservas
    else:
        form = ReservaForm()
    return render(request, 'core/criar_reserva.html', {'form': form})

# View para listar reservas
@login_required
def listar_reservas(request):
    reservas = Reserva.objects.all()  # Busca todas as reservas no banco de dados
    return render(request, 'core/listar_reservas.html', {'reservas': reservas})

# View para criar um aviso (acesso restrito a administradores)
@login_required
@user_passes_test(is_admin)
def criar_aviso(request):
    if request.method == 'POST':
        form = AvisoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avisos')
    else:
        form = AvisoForm()
    return render(request, 'core/criar_aviso.html', {'form': form})

# View para listar avisos
@login_required
def listar_avisos(request):
    avisos = Aviso.objects.all() 
    return render(request, 'core/avisos.html', {'avisos': avisos})

# View para editar um aviso
@login_required
@user_passes_test(is_admin)
def editar_aviso(request, id):
    aviso = get_object_or_404(Aviso, id=id)
    
    if request.method == 'POST':
        form = AvisoForm(request.POST, instance=aviso)
        if form.is_valid():
            form.save()
            return redirect('avisos')  # Redireciona após editar
    else:
        form = AvisoForm(instance=aviso)  # Preenche o formulário com os dados existentes

    return render(request, 'core/editar_aviso.html', {'form': form, 'aviso': aviso})

# View para confirmar a exclusão de um aviso
@login_required
@user_passes_test(is_admin)
def excluir_aviso(request, id):
    aviso = get_object_or_404(Aviso, id=id)
    if request.method == 'POST':
        aviso.delete()
        return redirect('avisos')  # Redireciona após a exclusão
    return render(request, 'core/confirm_delete.html', {'aviso': aviso})

# Views para renderizar páginas principais
@login_required
def home(request):
    return render(request, "core/home.html")

@login_required
def avisos(request):
    return listar_avisos(request)  # Reutiliza a função listar_avisos

@login_required
def registros(request):
    return render(request, "core/registros.html")

@login_required
def cobranca(request):
    return render(request, "core/cobranca.html")

@login_required
def reuniao(request):
    return render(request, "core/reuniao.html")

@login_required
def reserva(request):
    return listar_reservas(request)  # Reutiliza a função listar_reservas

@login_required
def configuracoes(request):
    return render(request, "core/configuracoes.html")

def login(request):
    return render(request, "core/login.html")
