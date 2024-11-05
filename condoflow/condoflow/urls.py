from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('avisos/', views.avisos, name='avisos'),
    path('registros/', views.registros, name='registros'),
    path('cobranca/', views.cobranca, name='cobranca'),
    path('reuniao/', views.reuniao, name='reuniao'),
    path('reserva/', views.reserva, name='reserva'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('login/', views.login, name='login'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
]