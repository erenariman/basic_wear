from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static

from .views import CustomerViewSet, ProductViewSet, OrderItemViewSet, OrderViewSet, ShippingAddressViewSet, CartViewSet, \
    CartItemViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-item', CartItemViewSet, basename='cart-item')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order-item', OrderItemViewSet, basename='order-item')
router.register(r'address', ShippingAddressViewSet, basename='address')

urlpatterns = router.urls
