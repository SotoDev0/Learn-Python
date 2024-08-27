from django.db import models

# Create your models here.

#Task
class Task(models.Model):
    description= models.CharField(max_length=100)