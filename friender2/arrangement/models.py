from django.db import models

# Create your models here.
SEX = [
    ('m', 'male'),
    ('f', 'female')
]
class Users(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=100, default='Minsk')

    def __str__(self):
        return self.name


stars = [
    ('1','good'), ('2','bad')
]
class User_establishment(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    category = models.CharField(choices=stars, max_length=1)
    phone = models.CharField(max_length=40)
    classification = models.CharField(max_length=40)

    def __str__(self):
        return self.name