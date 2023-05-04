from django.urls import path
from .views import *

#маршрутизация
urlpatterns = [
    path('site_rules/', site_rules),
    path('site_info/', site_info),
    path('main/', main_page, name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments/', place_arrangement, name='establishments'),
    path('rating/', rating, name='rating'),
    path('host/', host, name='host'),
    path('guest/', guest, name='guest'),
]