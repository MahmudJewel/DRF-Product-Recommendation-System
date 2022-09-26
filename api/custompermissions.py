from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user and request.user.groups.filter(name='CUSTOMER'):
			return True
		return False

class IsVendor(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user and request.user.groups.filter(name='VENDOR'):
			return True
		return False