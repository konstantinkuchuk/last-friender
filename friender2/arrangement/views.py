from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
import datetime
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admin/login/")
def main_page(request):
    return render(request, 'main.html')


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


def user_form_rating(request, **kwargs):
    user_id = int(kwargs['id'])
    context = {}
    if request.method == "POST":
        form = RatingUserForm(request.POST)
        context["form"] = form
        if form.is_valid():
            UserRating.objects.create(
                user_id=user_id,
                rating=request.POST['rating'],
                description=request.POST['description'],
            )
            return redirect("user_rating")
    else:
        form = RatingUserForm()
        context["form"] = form

    # context = {
    #     # "user": Users.objects.get(id=user_id)
    #     "form": form
    #
    # }
    return render(request, 'user_form_rating.html', context=context)


def create_user(request):
    context = {}
    if request.method == "POST":
        form = RatingUserForm(request.POST)
        context["form"] = form
        if form.is_valid():
            return redirect("user_rating")
    else:
        form = CreateUserForm()
        context["form"] = form

    # context = {
    #     # "user": Users.objects.get(id=user_id)
    #     "form": form
    #
    # }
    return render(request, 'create_user_form.html', context=context)


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world')

# class EstablishmentsCreateView(CreateView):
#     template_name = 'createplace.html'
#     model = User_establishment
#     fields = ['name', 'address', 'category', 'phone']
