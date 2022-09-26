from django.contrib import admin
from .models import User


lst = [User]
admin.site.register(lst)