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
    card_id = models.CharField(max_length=255, blank=True, null=True)
    last_pick = models.DateTimeField(blank=True, null=True)
    # location = models.TextField(blank=True, null=True)
    # device_id = models.CharField(max_length=500, blank=True, null=True)


class HistoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auditory = models.ForeignKey('schedule.Auditory', on_delete=models.CASCADE)
    last_pick = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}'