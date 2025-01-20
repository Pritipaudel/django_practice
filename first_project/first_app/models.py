from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField() django default
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null = True , blank=True)
    address = models.TextField(null = True , blank=True)
    image = models.ImageField()
    file = models.FileField()

class Marks(models.Model):
    pass