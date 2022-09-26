from django.contrib import admin
from .models import WeatherTypes, Product
# Register your models here.

lst = [WeatherTypes, Product]
admin.site.register(lst)