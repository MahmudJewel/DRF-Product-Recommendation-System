from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
User = get_user_model()

# from product.models import Product, WeatherTypes
# *********** start serializer for account create and update ************
class CustomerSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'password',
				  'first_name', 'last_name'] 

	# create overwrite for password hashing and grouping
	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.password = make_password(validated_data.get('password'))
		new_user.save()
		customer_group=Group.objects.get_or_create(name='CUSTOMER')
		customer_group[0].user_set.add(new_user)
		return new_user

class VendorSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'password',
				  'first_name', 'last_name']

	# create overwrite for password hashing and grouping
	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.password = make_password(validated_data.get('password'))
		new_user.save()
		customer_group=Group.objects.get_or_create(name='VENDOR')
		customer_group[0].user_set.add(new_user)
		return new_user
# *********** end serializer for account create and update ************
