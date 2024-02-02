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
        return self.customer.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.customer.name

    @property
    def get_order_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total() for item in orderitems])
        return total

    @property
    def get_order_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.product.name

    def get_total_price(self):
        total_price = self.product.price * self.quantity
        return total_price
