from rest_framework import serializers
from basic_wear.apps.store.models import Customer, Product, Order, OrderItem, ShippingAddress, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['customer', 'cart_items']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    addresses = ShippingAddressSerializer(many=True, read_only=True)
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['user', 'name', 'orders', 'addresses']
