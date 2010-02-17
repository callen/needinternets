from django.db import models

# Create your models here.

class ServiceProvider(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=30)

class Zipcode(models.Model):
    name = models.CharField(max_length=20)
    isp = models.ManyToManyField(ServiceProvider)
    
