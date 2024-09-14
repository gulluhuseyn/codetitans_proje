from django.db import models
from django.utils import timezone


# Create your models here.
class BlogComment(models.Model):
    author = models.CharField(max_length=150)
    email = models.ForeignKey("account.User",on_delete=models.CASCADE)
    comment = models.TextField()   
    
    def __str__(self):
        return f"{self.author}"