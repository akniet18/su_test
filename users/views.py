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


class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        s = LoginSer(data=request.data)
        if s.is_valid():
            username = s.validated_data['username']
            pwd = s.validated_data['password']
            user = User.objects.filter(username = username)
            if user.exists():
                user = user[0]
                if not user.check_password(pwd):
                    return Response({'status': 'wrong'})
                t, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        'status': 'ok',
                        "key": t.key, 
                        "uid": user.id,
                        "is_staff": user.is_staff,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'username': user.username,
                        # 'location': user.location,
                        'email': user.email,
                        'avatar': request.build_absolute_uri(user.avatar.url),
                        # 'birth_date': user.birth_date,
                        # 'device_id': user.device_id
                    }
                )
            else:
                return Response({'status': "wrong"})
        else:
            return Response(s.errors)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class History(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = HistoryModel.objects.filter(user__is_superuser=False).order_by('-last_pick')
        ser = HistorySer(users, many=True)
        return JsonResponse(ser.data, safe=False, json_dumps_params={'ensure_ascii':False})