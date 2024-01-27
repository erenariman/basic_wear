from django.urls import path
from rest_framework import routers

from .views import CustomerViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls
