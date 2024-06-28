from django.urls import path
from .views import ProductListView, ProductDetailView
from .api_views import ProductListAPIView

urlpatterns = [
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("api/products/", ProductListAPIView.as_view(), name="api_product_list"),
    path("", ProductListView.as_view(), name="product_list"),
]
