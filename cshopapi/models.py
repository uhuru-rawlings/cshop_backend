from django.db import models

# Create your models here.

class Registration(models.Model):
    useremail = models.EmailField(max_length=300)
    password = models.CharField(max_length=366)
    date_added = models.DateTimeField(auto_now=True)