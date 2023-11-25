from rest_framework import serializers
from .models import * 


class CheckUserSer(serializers.Serializer):
    number = serializers.CharField()

class CheckUserSer2(serializers.Serializer):
    id = serializers.CharField()
    card_id = serializers.CharField()
