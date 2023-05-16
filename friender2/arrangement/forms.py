from django import forms
from django.core.validators import *
from .models import Users

class RatingUserForm(forms.Form):
    rating = forms.IntegerField(
        validators=[MaxValueValidator(5,message='is to large rating'),
                    MinValueValidator(1,message='between 1 and 5')
                    ]
    )
    description =forms.CharField(validators=[
        MinLengthValidator(3,message='input more than 3 symbols')
    ])

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('email',)