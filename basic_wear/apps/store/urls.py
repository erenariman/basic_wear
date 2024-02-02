from django.urls import path
from rest_framework import routers

from .views import CustomerViewSet, ProductViewSet, OrderItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='order-items')

urlpatterns = router.urls
