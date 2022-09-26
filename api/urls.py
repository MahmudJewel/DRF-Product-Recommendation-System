from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewset, VendorViewset, WeatherViewset

router = DefaultRouter()
# Account creation, edition, deletions
router.register('auth/customer', CustomerViewset, basename='authcustomer')
router.register('auth/vendor', VendorViewset, basename='authvendor')
router.register('weather', WeatherViewset, basename='weather')


urlpatterns = [
    # router 
    path('', include(router.urls)),
]