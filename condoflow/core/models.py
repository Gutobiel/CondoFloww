from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    SINDICO = 'S'
    MORADOR = 'M'
    USER_TYPE_CHOICES = [
        (SINDICO, 'Síndico'),
        (MORADOR, 'Morador'),
    ]
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=MORADOR)

    groups = models.ManyToManyField(Group, related_name='core_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='core_user_set', blank=True)