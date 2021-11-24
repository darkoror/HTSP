from django.contrib import admin

from orders.models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'is_active', 'order_date',
    )
    list_filter = ('user', 'is_active', 'order_date',)


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = (
        'id', 'order', 'product', 'quantity',
    )
    list_filter = ('order', 'product', 'quantity',)
