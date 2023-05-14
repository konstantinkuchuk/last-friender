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
    email = models.EmailField(null=True)
    city = models.CharField(max_length=100, default='Minsk')

    # hobby = models.ManyToManyField("Hobbies", )
    class Meta:
        indexes = [
            models.Index(fields=["age", "name"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-name"]),
            models.Index(fields=["age"]),
            models.Index(fields=["-age"]),
            models.Index(fields=["name", "-sex"]),
            # models.Index(fields=["age", "sex"]),
        ]

    def __str__(self):
        return self.name


class Host(Users):
    max_spent_value = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Guest(Users):
    min_bill_value = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Passport(models.Model):
    passport_id = models.CharField(max_length=10, unique=True)
    date_create = models.DateTimeField(auto_now=datetime.utcnow())
    user = models.OneToOneField('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_id


class Hobbies(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=HOBBIES)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return str(self.name)


class Arrangements(models.Model):
    host = models.ForeignKey('Host', on_delete=models.CASCADE, null=True)
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, null=True)
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


class Rating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        abstract = True


class EstablishmentsRating(Rating):
    establishment = models.ForeignKey('User_establishment', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.establishment)


class UserRating(Rating):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rating)
