# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     email = models.EmailField(max_length=10,unique=True)

#     password = models.CharField(max_length=10)
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","first_name","last_name","password"]