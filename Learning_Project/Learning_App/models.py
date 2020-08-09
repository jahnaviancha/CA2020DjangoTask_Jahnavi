from django.db import models
from django.core import validators
from django import forms


# Create your models here.
def check(value):
    if len(value) < 6:
        raise forms.ValidationError("please enter at least 6 characters")
    # check for digit
    if not any(char.isdigit() for char in value):
        raise forms.ValidationError('Password must contain at least 1 digit.')

    # check for upper letter
    if not any(char.upper() for char in value):
        raise forms.ValidationError('Password must contain at least 1 uppercase letter.')

    # check for lower letter
    if not any(char.lower() for char in value):
        raise forms.ValidationError('Password must contain at least 1 lowercase letter.')

    # check for special character
    special_characters="[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    if not any(char in special_characters for char in value):
        raise forms.ValidationError('Password must contain at least 2 special char.')


def name(val):
    if val[0].lower() != 'a':
        raise forms.ValidationError("Name should start with 'a' ")


class Register(models.Model):
    name=models.CharField(max_length=40, validators=[name])
    email=models.EmailField(max_length=50)
    text=models.CharField(max_length=25)
    password=models.CharField(max_length=50, validators=[check])

    def __str__(self):
        return self.name
