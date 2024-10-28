from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin
    path("", auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),  # Página de login
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),  # Alternativa de login
    path("home/", views.home, name="home"),  # Página inicial após login
    path("avisos/", views.avisos, name="avisos"),  # Página de avisos
    path("registros/", views.registros, name="registros"),  # Página de registros
    path("cobranca/", views.cobranca, name="cobranca"),  # Página de cobranças
    path("reuniao/", views.reuniao, name="reuniao"),  # Página de reuniões
    path("reserva/", views.reserva, name="reserva"),  # Página de reservas
    path("configuracoes/", views.configuracoes, name="configuracoes"),  # Página de configurações
]
