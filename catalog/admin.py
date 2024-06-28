from django.contrib import admin
from .models import Product, ProductAttribute, ProductAttributeValue

admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
