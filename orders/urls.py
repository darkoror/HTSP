from django.urls import path
from orders import views

app_name = 'order'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),
    path('<int:order_item_id>/remove_item/', views.RemoveOrderItemView.as_view(), name='remove-order-item'),
    path('order/', views.MakeOrderView.as_view(), name='make-order'),
]
