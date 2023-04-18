from django.shortcuts import render

from django.http import HttpResponse
import datetime


#функция представления views
def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)

def greeting(request, name):
    return HttpResponse(f"<h1>Hello {name}</h1>")

def site_rules(request):
    return HttpResponse(f"""<h1>Правильно заполните анкету ...
Блокируйте без зазрения совести ...
Созванивайтесь в течение одного-трех дней ...
Назначайте встречу не сразу, а через 5 дней ...
Встречайтесь не чаще чем раз в 5 дней ...
Старайтесь лучше узнать партнера ...
Уважайте свои границы ...
Будьте собой</h1>""" )

def site_info(request):
    return HttpResponse(f'<h1>info not found ;)</h1>')

