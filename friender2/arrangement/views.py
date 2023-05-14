from django.shortcuts import render

from django.http import HttpResponse
from .models import *
import datetime


# friends = {"Max":[34,'max@mail.ru'],
#            "Grigory":[28,'grigory@mail.ru'],
#            "Anna":[37,'anna@mail.ru'],
#            "Pedro":[23,'pedro@mail.ru'],
#            "Kate":[19,'kate@mail.ru']
#            }
# establishments = ['Butter bro', 'Terra', 'Golden Cafe', 'Pancakes', 'Depo']


# функция представления views


def all_friends(request):
    context = {
        "friends": Users.objects.filter()[:10].prefetch_related("hobbies_set", "userrating_set")

    }
    return render(request, 'friends.html', context=context)


def main_page(request):
    return render(request, 'main.html')


def place_arrangement(request):
    context = {
        "establishments": User_establishment.objects.all(),

    }
    return render(request, 'establishments.html', context=context)


# def static_url(request):
#     return render(request, "static_example.html")

# def guest(request):
#     return render(request, 'guest.html')


# def host(request):
#     return render(request, 'host.html')


# def user_rating(request):
#     return render(request, 'userrating.html')


def user_rating(request):
    context = {
        "ratings": Users.objects.filter(age__gte=28)[:100],

    }
    return render(request, 'userrating.html', context=context)
