from django.contrib import admin

from .models import (
    Product,
    Category,
    ProductImage
)


class TabularInLineImage(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ['image']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [TabularInLineImage, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)