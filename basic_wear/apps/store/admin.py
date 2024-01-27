from django.contrib import admin
from .models import Customer, Product, ShippingAddress, Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(Order)
