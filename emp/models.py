from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 100, null = True)
    phone = models.CharField(max_length = 100, null = True)


    def __str__(self):
        return str(self.name) or ''


