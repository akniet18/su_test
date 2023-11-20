from rest_framework import serializers
from .models import * 


class CheckUserSer(serializers.Serializer):
    number = serializers.CharField()
