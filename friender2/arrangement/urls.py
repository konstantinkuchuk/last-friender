from django.urls import path
from .views import *

#маршрутизация
urlpatterns = [
    path('time_now/', current_datetime),
    path('greeting/<str:name>/', greeting),
    path('site_rules/', site_rules),
    path('site_info/', site_info)
]