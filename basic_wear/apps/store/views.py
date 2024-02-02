from django.shortcuts import render
from rest_framework import request

from .models import Customer, Product, Order, OrderItem
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer, ProductSerializer, OrderItemSerializer,OrderSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    """
    def perform_create(self, serializer):
        customer = self.request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
        serializer.save(order=order)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
            return OrderItem.objects.filter(order=order)
        else:
            return OrderItem.objects.none()

    """


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items}

    return render(request, 'store/cart.html', context)
