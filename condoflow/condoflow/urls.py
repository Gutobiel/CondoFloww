
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),  # Admin
    path("", auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),  # Página de login
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),  # Alternativa de login
    path("home/", views.home, name="home"),  # Página inicial após login
    path('avisos/', views.listar_avisos, name='avisos'),
    path('avisos/criar', views.criar_aviso, name='criar_aviso'),
    path('avisos/<int:id>/delete/', views.excluir_aviso, name='excluir_aviso'),
    path('avisos/<int:id>/editar/', views.editar_aviso, name='editar_aviso'),
    path("registros/", views.registros, name="registros"),  # Página de registros
    path("cobranca/", views.cobranca, name="cobranca"),  # Página de cobranças
    path("reuniao/", views.reuniao, name="reuniao"),  # Página de reuniões
    path("reserva/", views.reserva, name="reserva"),  # Página de reservas
    path("configuracoes/", views.configuracoes, name="configuracoes"),  # Página de configurações
]

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