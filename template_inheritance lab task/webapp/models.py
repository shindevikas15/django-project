from django.db import models
from django.core import validators


# Create your models here.

class EmpFresher(models.Model):
    name=models.CharField(max_length=20)
    Email_ID = models.EmailField()

    # attrs = {"type": "password"}
    # password = models.CharField(widget=models.TextInput(attrs=attrs))

    phone_number = models.CharField(max_length=12)
    location=models.CharField(max_length=40)
    # resume=models.FileField()


class EmpProfessional(models.Model):
    name=models.CharField(max_length=20)
    Email_ID =models.EmailField()

   # attrs = {"type": "password"}
    #password = models.CharField(widget=models.TextInput(attrs=attrs))

    phone_number = models.CharField(max_length=12)
    location=models.CharField(max_length=40)
    # upload_your_experience_certificate_here=models.FileField()
    # resume= models.FileField()

