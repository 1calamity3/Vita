from django.contrib import admin
from .models import Category, Product, Order, OrderItem, SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
