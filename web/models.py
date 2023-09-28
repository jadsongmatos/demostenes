"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nova_coluna = models.CharField(max_length=200, null=True, blank=True)
    
    # Altere os related_names aqui
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="customuser_set",  # related_name personalizado
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customuser_set",  # related_name personalizado
        related_query_name="customuser",
    )
"""