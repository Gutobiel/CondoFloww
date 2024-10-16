from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path("home/", views.home, name="home"),
    path("avisos/", views.avisos, name="avisos"),
    path("registros/", views.registros, name="registros"),
    path("cobranca/", views.cobranca, name="cobranca"),
    path("reuniao/", views.reuniao, name="reuniao"),
    path("reserva/", views.reserva, name="reserva"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
]