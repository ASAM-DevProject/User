from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    # for example
    phone = models.CharField(max_length=12)
    National_Code = models.CharField(max_length=10)