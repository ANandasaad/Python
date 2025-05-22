from django.db import models

# Create your models here.
class Feature(models.Model):
    heading = models.CharField(max_length=100)
    subHeading = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    
