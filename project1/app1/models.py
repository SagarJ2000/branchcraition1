from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name =models.CharField(max_length=66)
    lname = models.CharField(max_length=66)
    