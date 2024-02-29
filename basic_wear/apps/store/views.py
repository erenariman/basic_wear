from .models import Customer, Product, Order, OrderItem, ShippingAddress, Cart, CartItem
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin,
                                   DestroyModelMixin)
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer, ProductSerializer, OrderItemSerializer, OrderSerializer, \
    ShippingAddressSerializer, CartSerializer, CartItemSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]


class ShippingAddressViewSet(ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsAuthenticated]


class CartViewSet(CreateModelMixin,
                  UpdateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Cart.objects.get(customer=self.request.user.customer)


class CartItemViewSet(CreateModelMixin,
                      UpdateModelMixin,
                      ListModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.customer.cart)
