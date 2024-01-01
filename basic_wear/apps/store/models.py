from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200, null=True)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE)
    total_price = models.FloatField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.customer


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
