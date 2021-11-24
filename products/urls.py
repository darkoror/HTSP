from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/add_to_order/', views.AddToOrderView.as_view(), name='add-to-order')
]
