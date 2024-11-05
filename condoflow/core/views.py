from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login



def home(request):
    return render(request, 'core/home.html')

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Usuário ou senha incorretos'})
    return render(request, 'core/login.html')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'core/user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/user_form.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User
from .forms import CustomUserChangeForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User
from .forms import CustomUserChangeForm

@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'user_type': user.user_type,
            })
    return render(request, 'core/user_form.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'core/user_confirm_delete.html', {'user': user})