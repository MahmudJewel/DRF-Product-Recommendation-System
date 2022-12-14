from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import JsonResponse
import os

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
	IsAuthenticated, 
	IsAdminUser, 
	IsAuthenticatedOrReadOnly, 
	AllowAny
)
from rest_framework import status
from rest_framework import generics


from django.contrib.auth import get_user_model
User = get_user_model()

import json
import urllib.request

from .serializers import (
	CustomerSerializers, 
	VendorSerializers, 
	WeatherSerializers, 
	ProductSerializers
)

from product.models import WeatherTypes, Product
from .custompermissions import IsCustomer, IsVendor


# Create your views here.

# Customer creation, edition, deletion through viewset
class CustomerViewset(viewsets.ModelViewSet):
	serializer_class = CustomerSerializers
	queryset = User.objects.filter(groups__name='CUSTOMER')
	# queryset = Group.objects.get(name="CUSTOMER").user_set.all()

	def get_permissions(self):
		if self.request.method == 'POST':
			self.permission_classes = [AllowAny, ]
		else:
			self.permission_classes = [IsAdminUser, ]
		return super(CustomerViewset, self).get_permissions()


# Vendor creation, edition, deletion through viewset
class VendorViewset(viewsets.ModelViewSet):
	serializer_class = VendorSerializers
	queryset = User.objects.filter(groups__name='VENDOR')

	def get_permissions(self):
		if self.request.method == 'POST':
			self.permission_classes = [AllowAny, ]
		else:
			self.permission_classes = [IsAdminUser, ]
		return super(VendorViewset, self).get_permissions()

# product/weather types view for creation, edition, deletions 
class WeatherViewset(viewsets.ModelViewSet):
	serializer_class = WeatherSerializers
	queryset = WeatherTypes.objects.all()
	permission_classes = [IsAdminUser, ]

# product creation, edition, deletion 
class ProductViewset(viewsets.ModelViewSet):
	serializer_class = ProductSerializers
	queryset = Product.objects.all()
	# permission_classes = [AllowAny, ]
	def get_permissions(self):
		if self.request.method == 'GET':
			self.permission_classes = [IsAuthenticated, ]

		elif self.request.method == 'PATCH':
			self.permission_classes = [IsAdminUser, ]
		
		else:
			self.permission_classes = [IsVendor, ]
		return super(ProductViewset, self).get_permissions()

# product search view
class ProductSearch(generics.ListAPIView):
	serializer_class = ProductSerializers
	permission_classes = [IsAuthenticated, ]

	def get_queryset(self):
		search = self.request.query_params.get('search', None)
		products = Product.objects.all()
		if search is not None:
			products = products.filter(title__contains=search) | products.filter(types__title__contains=search)
		return products
	
# product recommendation using open weather 
class ProductRecommendation(generics.ListAPIView):
	serializer_class = ProductSerializers
	permission_classes = [AllowAny, ]

	def get_queryset(self):
		location = self.request.query_params.get('location', None)
		products = Product.objects.all()
		if location is not None:
			API_KEY=str(os.getenv('OPENWEATHER_API_KEY'))
			# print('API key => ',API_KEY)
			try:
				res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+API_KEY).read()
				json_data = json.loads(res)
				temperature = int(json_data['main']['temp'] - 273.15)
				# temperature = 10
				print('temperature: ', temperature)
				products = products.filter(types__low_temp__lte=temperature).filter(types__high_temp__gte=temperature)
			except Exception as e:
				print('Error==> ', e)
		return products