from django.contrib import admin
from .models import Customer, Product, ShippingAddress, Order, OrderItem, Cart, CartItem

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
