from django.contrib import admin

from products.models import Product, Country, ProductType


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'country_producer', 'type', 'price',
    )
    list_filter = ('name', 'country_producer', 'type', 'price',)


@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )
    list_filter = ('name',)


@admin.register(ProductType)
class AdminProductType(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )
    list_filter = ('name',)
