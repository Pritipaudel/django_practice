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

class flower(models.Model):
    name = models.CharField(max_length= 50)
    f_color = models.CharField(max_length = 50)
    number = models.IntegerField()

    def __str__(self):
        return f"Flower: {self.name}, Color: {self.f_color}, Quantity: {self.number}"
