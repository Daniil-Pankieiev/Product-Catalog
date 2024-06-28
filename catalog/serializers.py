from rest_framework import serializers
from .models import Product, ProductAttributeValue


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute = serializers.StringRelatedField()

    class Meta:
        model = ProductAttributeValue
        fields = ["attribute", "value"]


class ProductSerializer(serializers.ModelSerializer):
    attributes = ProductAttributeValueSerializer(
        source="productattributevalue_set", many=True, read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "description",
            "stylized_description",
            "image",
            "attributes",
        ]
