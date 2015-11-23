from django.db import models

# Create your models here.

class Flower(models.Model):
    image = models.ImageField(upload_to='static/flowers', null=True, blank=True)
    image_type = models.TextField(max_length=30,default="square")
    
    def __unicode__(self):
		return  self.image_type