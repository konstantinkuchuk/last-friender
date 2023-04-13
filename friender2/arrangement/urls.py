from django.urls import path
from .views import *

#маршрутизация
urlpatterns = [
    path('time_now/', current_datetime),
    path('greeting/<str:name>/', greeting),
]