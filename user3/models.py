from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    last_failed_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.first_name} {self.last_name}'



