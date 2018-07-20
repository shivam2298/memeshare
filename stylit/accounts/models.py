from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, related_name="profile",on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name="followers",null=True,blank=True)