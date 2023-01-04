from uuid import uuid4

from django.db import models


class User(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=64, verbose_name='username')
    firstname = models.CharField(max_length=64, verbose_name='first_name')
    lastname = models.CharField(max_length=64, verbose_name='last_name')
    email = models.EmailField(unique=True, verbose_name='email')
    birthday = models.DateField(verbose_name='birthday')
