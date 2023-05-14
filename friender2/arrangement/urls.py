from django.urls import path
from .views import *

#маршрутизация
urlpatterns = [
    path('main/', main_page, name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments/', place_arrangement, name='establishments'),
    path('user_rating/', user_rating, name='user_rating'),
]