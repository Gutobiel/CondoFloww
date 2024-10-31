from django.db import models
from django.contrib.auth.models import User

""" Reservas """
class Reserva(models.Model):
    AREA_CHOICES = [
        ('Churrasqueira', 'Churrasqueira'),
        # Adicione outras áreas conforme necessário
    ]

    area = models.CharField(max_length=50, choices=AREA_CHOICES)
    data = models.DateField()
    horario = models.TimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.area} - {self.data} - {self.horario}"
""" Reservas """

""" Avisos """
class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
""" Avisos """
