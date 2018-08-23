from django.db import models


class UserInfo(models.Model):
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=32)
    # mobie =models.CharField(max_length=11)


# Create your models here.
