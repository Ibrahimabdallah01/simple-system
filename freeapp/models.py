from msilib.schema import SelfReg
from typing import Self
from django.db import models

# Create your models here.


class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=150)

    # def __str__(self@Record):
    # return SelfReg.first_name + "   " + Self.last_name
    def __str__(self):
        return self.first_name + "   " + self.last_name
