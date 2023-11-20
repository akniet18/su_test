from django.urls import path
from .views import *

urlpatterns = [
    path('check/', CheckUserInAudience.as_view())
]