from django.db import models

# Create your models here.

class Flower(models.Model):
    image = models.ImageField(upload_to='static/flowers', null=True, blank=True)