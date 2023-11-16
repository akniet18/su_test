from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime


def user_photos_dir(instanse, filename):
    usrnme = f'{instanse.username}'
    folder_name = f"{usrnme}/{datetime.today().strftime('%d_%m_%Y')}/{filename}"
    return folder_name


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=user_photos_dir, blank=True, null=True, default="default/default.png")
    # location = models.TextField(blank=True, null=True)
    # device_id = models.CharField(max_length=500, blank=True, null=True)