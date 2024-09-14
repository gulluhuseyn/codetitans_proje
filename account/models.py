from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","first_name","last_name","password"]


from django.db import models
from datetime import timezone
import pyotp

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return (self.created_at - timezone.now()).total_seconds() < 300
