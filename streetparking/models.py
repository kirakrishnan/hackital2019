from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.BigIntegerField()
    image_no = models.CharField(max_length=200)
    name_plate = models.CharField(max_length=200)
    def __str__(self):
        return self.name


