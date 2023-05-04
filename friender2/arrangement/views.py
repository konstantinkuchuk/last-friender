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


def site_rules(request):
    return HttpResponse(f"""<h1>Правильно заполните анкету ...
Блокируйте без зазрения совести ...
Созванивайтесь в течение одного-трех дней ...
Назначайте встречу не сразу, а через 5 дней ...
Встречайтесь не чаще чем раз в 5 дней ...
Старайтесь лучше узнать партнера ...
Уважайте свои границы ...
Будьте собой</h1>""")


def site_info(request):
    return HttpResponse(f'<h1>info not found ;)</h1>')


def all_friends(request):
    context = {
        "friends": Users.objects.filter(age__gte=28)[:100],

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

def guest(request):
    return render(request, 'guest.html')


def host(request):
    return render(request, 'host.html')


def rating(request):
    return render(request, 'rating.html')
