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

