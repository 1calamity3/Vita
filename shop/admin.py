from django.contrib import admin
from .models import Category, Product, Order, OrderItem, SubCategory
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from .models import Product
from django.http import HttpResponseRedirect
from django.urls import path


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(OrderItem)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'duplicate_link')  # Show duplicate button in list

    def duplicate_link(self, obj):
        url = reverse('admin:shop_product_duplicate', args=[obj.pk])  # Use correct namespace
        return format_html('<a href="{}" class="button">Duplicate</a>', url)

    duplicate_link.short_description = "Duplicate"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/duplicate/', self.admin_site.admin_view(self.duplicate_object_view), name="shop_product_duplicate"),
        ]
        return custom_urls + urls

    def duplicate_object_view(self, request, pk):
        obj = Product.objects.get(pk=pk)
        obj.pk = None  # Reset PK to create a new object
        obj.save()
        self.message_user(request, _("Product duplicated successfully."))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/shop/product/'))


class ProductModelAdmin(admin.ModelAdmin):
    # ...

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('duplicate/<int:pk>/', self.admin_site.admin_view(self.duplicate_object_view), name="duplicate_object"),
        ]
        return custom_urls + urls

    def duplicate_object_view(self, request, pk):
        obj = Product.objects.get(pk=pk)
        obj.pk = None
        obj.save()
        self.message_user(request, _("Object duplicated successfully."))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
