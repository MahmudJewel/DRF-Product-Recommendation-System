from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import Group
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import CustomerSerializers, VendorSerializers, WeatherSerializers, ProductSerializers
from product.models import WeatherTypes, Product
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
	permission_classes = [AllowAny, ]

class ProductViewset(viewsets.ModelViewSet):
	serializer_class = ProductSerializers
	queryset = Product.objects.all()
	permission_classes = [AllowAny, ]
