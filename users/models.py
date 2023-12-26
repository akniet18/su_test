from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime


def user_photos_dir(instanse, filename):
    usrnme = f'{instanse.username}'
    folder_name = f"{usrnme}/{datetime.today().strftime('%d_%m_%Y')}/{filename}"
    return folder_name

class CustomManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
            values = [email, username]
            field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
            for field_name, value in field_value_map.items():
                if not value:
                    raise ValueError('The {} value must be set'.format(field_name))

            email = self.normalize_email(email)
            user = self.model(
                email=email,
                username=username,
                **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
            return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, username, password, **extra_fields)

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username,  password, **extra_fields)

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=user_photos_dir, blank=True, null=True, default="default/default.png")
    card_id = models.CharField(max_length=255, blank=True, null=True)
    last_pick = models.DateTimeField(blank=True, null=True)

    objects = CustomManager()
    # location = models.TextField(blank=True, null=True)
    # device_id = models.CharField(max_length=500, blank=True, null=True)


class HistoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auditory = models.ForeignKey('schedule.Auditory', on_delete=models.CASCADE)
    last_pick = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}'