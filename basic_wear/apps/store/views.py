from rest_framework import exceptions
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Cart, CartItem
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin,
                                   DestroyModelMixin)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CustomerSerializer, ProductSerializer, OrderItemSerializer, OrderSerializer, \
    ShippingAddressSerializer, CartSerializer, CartItemSerializer


class CustomerViewSet(CreateModelMixin,
                      UpdateModelMixin,
                      RetrieveModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        if self.request.user.is_authenticated:
            try:
                return Customer.objects.get(user=self.request.user)
            except Customer.DoesNotExist:
                # If Customer object doesn't exist for the authenticated user
                raise exceptions.NotFound("Customer not found.")
        else:
            # Handle case where user is not authenticated
            raise exceptions.NotAuthenticated("User is not authenticated.")


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [AllowAny]


class ShippingAddressViewSet(ModelViewSet):
    serializer_class = ShippingAddressSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ShippingAddress.objects.filter(customer=self.request.user.customer)


class CartViewSet(CreateModelMixin,
                  UpdateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return Cart.objects.get(customer=self.request.user.customer)


class CartItemViewSet(CreateModelMixin,
                      UpdateModelMixin,
                      ListModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.customer.cart)
