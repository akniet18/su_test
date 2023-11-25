from django.urls import path
from .views import *

urlpatterns = [
    path('check/', CheckUserInAudience.as_view()),
    path('check2/', CheckUserInAudience2.as_view())
]