from django.urls import path, re_path
from .views import *

#маршрутизация
urlpatterns = [
    path('main/', main_page, name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments/', place_arrangement, name='establishments'),
    path('user_rating/', user_rating, name='user_rating'),
    re_path(r"^rating_user/(?P<id>[0-9]+)$", user_form_rating, name="user_from_rating"),
    path('create_user/', create_user, name='create_user'),
]