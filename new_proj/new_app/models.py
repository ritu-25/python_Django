from django.db import models

# Create your models here.
class contact(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_no = models.IntegerField(max_length=50)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin_code = models.IntegerField(max_length=50)