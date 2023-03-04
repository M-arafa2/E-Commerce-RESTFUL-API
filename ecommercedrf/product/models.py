from django.db import models

# Create your models here.
class Brand(models.Model):
    brand = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    

