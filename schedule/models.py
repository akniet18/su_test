from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Auditory(models.Model):
    number = models.CharField(max_length=255)
    corpus = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.corpus} - {self.number}'

class Schedule(models.Model):
    audience = models.ForeignKey(Auditory, on_delete=models.CASCADE, related_name='audiences')
    students = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.audience}'
