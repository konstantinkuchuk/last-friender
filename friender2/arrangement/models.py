from django.db import models
from datetime import datetime

# Create your models here.
SEX = [
    ('m', 'male'),
    ('f', 'female')
]

HOBBIES = [
    ('sp', 'sport'),
    ('tr', 'traveling'),
    ('pt', 'painting'),
    ('cg', 'computer_games'),
    ('sh', 'shoping'),
    ('ph', 'photo'),
    ('ms', 'music')
]


class Users(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=100, default='Minsk')
    # hobby = models.ManyToManyField("Hobbies", )

    def __str__(self):
        return self.name

class Passport(models.Model):
    passport_id = models.CharField(max_length=10, unique=True)
    date_create = models.DateTimeField(auto_created=datetime.now())
    user = models.OneToOneField('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_id

class Hobbies(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=HOBBIES)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return str(self.name)

class UserRating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey('Users',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Arrangements(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    # user2 = models.ForeignKey('Users', on_delete=models.CASCADE)
    establishments = models.ForeignKey('User_establishment', on_delete=models.CASCADE)


CATEGORY = [
    ('c', 'cafe'), ('r', 'restaurant'), ('p', 'pub')
]


class User_establishment(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    category = models.CharField(choices=CATEGORY, max_length=1)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class EstablishmentsRating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    establishment = models.ForeignKey('User_establishment', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.establishment)
