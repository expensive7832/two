from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=11)
    first_name = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)