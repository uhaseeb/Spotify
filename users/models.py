from django.db import models
from django.contrib.auth.models import AbstractUser
from . import constants


class User(AbstractUser):
    gender = models.CharField(max_length=30, choices=constants.gender_choice, default='Male')


