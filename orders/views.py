from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin

from orders.models import Order, OrderItem


class RemoveOrderItemView(LoginRequiredMixin, View):
    def post(self, request, order_item_id):
        order, _ = Order.objects.get_or_create(user=request.user, is_active=True)
        order_item = get_object_or_404(OrderItem, id=order_item_id, order=order)
        order_item.delete()
        messages.info(request, "Товар вилучено з кошика.")
        return redirect("order:order-list")


class OrderListView(LoginRequiredMixin, MultipleObjectTemplateResponseMixin, BaseListView):
    model = OrderItem
    template_name = 'orders/order_list.html'
    success_url = reverse_lazy('order:order-list')

    def get_queryset(self):
        order, _ = Order.objects.get_or_create(user=self.request.user, is_active=True)
        return self.model.objects.filter(order=order.pk)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(OrderListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['order'] = Order.objects.get(user=self.request.user, is_active=True)
        return context


class MakeOrderView(LoginRequiredMixin, View):
    def post(self, request):
        order, _ = Order.objects.get_or_create(user=request.user, is_active=True)
        if not order.items.all():
            messages.info(request, "Ваша корзина пуста.")
            return redirect("order:order-list")
        order.is_active = False
        order.order_date = timezone.now()
        order.save()

        Order.objects.create(user=request.user, is_active=True)
        messages.success(request, f"Ви успішно оформили замовлення на суму {order.total_price} грн.")
        return redirect("order:order-list")
