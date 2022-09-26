from django.db import models

# Create your models here.

class WeatherTypes(models.Model):
    title=models.CharField(max_length=200,null=True, blank=True)
    low_temp = models.IntegerField(null=True, blank=True)
    high_temp = models.IntegerField(null=True, blank=True)

class Product(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title=models.CharField(max_length=200,null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    types = models.ForeignKey(WeatherTypes, on_delete=models.SET_DEFAULT, default='normal')
    