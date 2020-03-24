from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)


class UserP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images', null=True)
    professional_profile = models.CharField(max_length=100)


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(UserP, null=True, on_delete=models.PROTECT)
