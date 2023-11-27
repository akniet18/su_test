from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import * 
import json
from django.http import JsonResponse
from .serializers import *
from users.models import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework import generics, permissions, status, views
from django.conf import settings
import serial
from datetime import datetime    

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
            user = User.objects.filter(card_id = s.validated_data['card_id'])
            if user:
                auditory = Auditory.objects.filter(auditory_id = s.validated_data['id'])
                if auditory:
                    history = HistoryModel.objects.get_or_create(user=user[0], auditory = auditory[0])
                    history[0].last_pick = datetime.now()
                    history[0].save()
                    schedule = Schedule.objects.filter(audience = auditory[0])
                    if schedule:
                        if user[0] in schedule[0].students.all():
                            history[0].status = 1
                            history[0].save()
                            user[0].last_pick = datetime.now()
                            user[0].save()
                            return Response({'status': "ok"})
                        else:
                            history[0].status = 0
                            history[0].save()
                            return Response({'status': 'not found'})
                    else:
                        return Response({'status': 'not found'})
                else:
                    return Response({'status': 'not found'})
            else:
                return Response({'status': 'not found'})
        else:
            return Response(s.errors)