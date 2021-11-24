from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin

# from basket.models import Basket
from products.filters import ProductFilter
from products.models import Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Get specific product"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products:product-detail')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])


# class AddToBasketView(LoginRequiredMixin, View):
#     """add to logic to add item to basket"""
#     def post(self, request, pk):
#         basket, _ = Basket.objects.get_or_create(user=request.user, is_active=True)
#         product = get_object_or_404(Product, id=pk)
#         basket_item, created = basket.items.get_or_create(product=product)
#         if not created:
#             basket_item.quantity += 1
#             basket_item.save()
#             messages.info(request, "Товар оновлено.")
#         else:
#             messages.info(request, "Товар додано в корзину.")
#             pass
#         return redirect("products:product-detail", pk)


class ProductListView(LoginRequiredMixin, MultipleObjectTemplateResponseMixin, BaseListView):
    """Get list of products"""
    model = Product
    filterset_class = ProductFilter
    template_name = 'products/product_list.html'
    success_url = reverse_lazy('products:product-list')

    def get_queryset(self):
        queryset = self.model.objects.filter(type__isnull=False)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context
