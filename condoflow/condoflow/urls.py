from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("avisos/", views.avisos, name="avisos"),
    path("registros/", views.registros, name="registros"),
    path("cobranca/", views.cobranca, name="cobranca"),
    path("reuniao/", views.reuniao, name="reuniao"),
    path("reserva/", views.reserva, name="reserva"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
    path("login/", views.login, name="login"),
]