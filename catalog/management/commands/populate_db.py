from django.core.management.base import BaseCommand
from catalog.models import Product, ProductAttribute, ProductAttributeValue
from django.utils.text import slugify
import random


class Command(BaseCommand):
    help = "Populate the database with example data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        ProductAttributeValue.objects.all().delete()
        ProductAttribute.objects.all().delete()
        Product.objects.all().delete()

        # Create attributes
        color_attr = ProductAttribute.objects.create(name="Color", slug="color")
        size_attr = ProductAttribute.objects.create(name="Size", slug="size")

        colors = ["Red", "Green", "Blue"]
        sizes = ["Small", "Medium", "Large"]

        # Create products and their attributes
        for i in range(10):
            product_name = f"Product {i + 1}"
            product = Product.objects.create(
                name=product_name,
                slug=slugify(product_name),
                description=f"This is a description for {product_name}.",
                stylized_description=f"<strong>This</strong> is a <em>stylized</em> description for {product_name}.",
                image="path/to/image.jpg",
            )

            # Add color attributes
            color_value = random.choice(colors)
            ProductAttributeValue.objects.create(
                product=product, attribute=color_attr, value=color_value
            )

            # Add size attributes
            size_value = random.choice(sizes)
            ProductAttributeValue.objects.create(
                product=product, attribute=size_attr, value=size_value
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with example data")
        )
