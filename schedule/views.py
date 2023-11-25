from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import * 
import json
from django.http import JsonResponse
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework import generics, permissions, status, views
from django.conf import settings
import serial

class CheckUserInAudience(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        s = CheckUserSer(data=request.data)
        if s.is_valid():
            number = s.validated_data['number']
            user = request.user
            auditory = Auditory.objects.get(number = number)
            schedule = Schedule.objects.get(audience = auditory)
            if user in schedule.students.all():
                return Response({'status': "ok"})
            else:
                return Response({'status': 'not found'})
        else:
            return Response(s.errors)


class CheckUserInAudience2(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        s = CheckUserSer2(data=request.data)
        if s.is_valid():
            print(s.validated_data)
            user = User.objects.get(card_id = s.validated_data['card_id'])
            auditory = Auditory.objects.get(auditory_id = s.validated_data['id'])
            schedule = Schedule.objects.get(audience = auditory)
            if user in schedule.students.all():
                return Response({'status': "ok"})
            else:
                return Response({'status': 'not found'})
        else:
            return Response(s.errors)