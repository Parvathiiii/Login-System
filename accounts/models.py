from django.db import models

# Create your models here.

class LoginDetails(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
