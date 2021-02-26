from django.db import models

# Create your models here.
class Piza(models.Model):
    name=models.CharField(max_length=100)
    types = models.CharField(max_length=100)

class Size(models.Model):
    pname = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

class Toping(models.Model):
    toping = models.CharField(max_length=100)