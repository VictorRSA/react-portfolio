from django.db import models
from django.contrib.auth.models import AbstractUser


#  Create your models here.

class users(AbstractUser):
    id =models.AutoField(max_length=11,primary_key=True)
    full_name = models.CharField(max_length=60,blank=False)
    username = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=20,blank=False)
    date = models.DateField(null=True)

class Register(AbstractUser):
    id =models.AutoField(max_length=11,primary_key=True)
    full_name = models.CharField(max_length=60,blank=False)
    username = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=20,blank=False)
    date = models.DateField(null=True)