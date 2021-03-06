from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    website = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    pin = models.CharField(max_length=500)
    useridas =models.CharField(max_length=500)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
    website = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    pin = models.CharField(max_length=100, default='')

    USERNAME_FIELD = 'website'
