from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', RegisterView.as_view()),
    path('history/', History.as_view()),
]