from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from catalog.models import Product, ProductAttribute, ProductAttributeValue
from django.utils.text import slugify


class ProductModelTests(TestCase):

    def setUp(self):
        self.color_attr = ProductAttribute.objects.create(name="Color", slug="color")
        self.size_attr = ProductAttribute.objects.create(name="Size", slug="size")

    def test_product_creation(self):
        product = Product.objects.create(
            name="Product 1",
            slug=slugify("Product 1"),
            description="This is a description for Product 1.",
            stylized_description="<strong>This</strong> is a <em>stylized</em> description for Product 1.",
            image="path/to/image.jpg",
        )
        self.assertEqual(product.name, "Product 1")
        self.assertEqual(product.slug, "product-1")

    def test_product_attribute_value_creation(self):
        product = Product.objects.create(
            name="Product 1",
            slug=slugify("Product 1"),
            description="This is a description for Product 1.",
            stylized_description="<strong>This</strong> is a <em>stylized</em> description for Product 1.",
            image="path/to/image.jpg",
        )
        ProductAttributeValue.objects.create(
            product=product, attribute=self.color_attr, value="Red"
        )
        ProductAttributeValue.objects.create(
            product=product, attribute=self.size_attr, value="Medium"
        )

        attributes = product.productattributevalue_set.all()
        self.assertEqual(attributes.count(), 2)
        self.assertEqual(attributes[0].value, "Red")
        self.assertEqual(attributes[1].value, "Medium")


class ProductViewTests(TestCase):

    def setUp(self):
        self.color_attr = ProductAttribute.objects.create(name="Color", slug="color")
        self.size_attr = ProductAttribute.objects.create(name="Size", slug="size")
        self.product = Product.objects.create(
            name="Product 1",
            slug=slugify("Product 1"),
            description="This is a description for Product 1.",
            stylized_description="<strong>This</strong> is a <em>stylized</em> description for Product 1.",
            image="path/to/image.jpg",
        )
        ProductAttributeValue.objects.create(
            product=self.product, attribute=self.color_attr, value="Red"
        )
        ProductAttributeValue.objects.create(
            product=self.product, attribute=self.size_attr, value="Medium"
        )

    def test_product_detail_view(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product 1")
        self.assertContains(
            response,
            "<strong>This</strong> is a <em>stylized</em> description for Product 1.",
            html=True,
        )
        self.assertContains(response, "Red")
        self.assertContains(response, "Medium")


class ProductAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.color_attr = ProductAttribute.objects.create(name="Color", slug="color")
        self.size_attr = ProductAttribute.objects.create(name="Size", slug="size")
        self.product = Product.objects.create(
            name="Product 1",
            slug=slugify("Product 1"),
            description="This is a description for Product 1.",
            stylized_description="<strong>This</strong> is a <em>stylized</em> description for Product 1.",
            image="path/to/image.jpg",
        )
        ProductAttributeValue.objects.create(
            product=self.product, attribute=self.color_attr, value="Red"
        )
        ProductAttributeValue.objects.create(
            product=self.product, attribute=self.size_attr, value="Medium"
        )

    def test_get_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Product 1")
        self.assertEqual(response.data[0]["attributes"][0]["attribute"], "Color")
        self.assertEqual(response.data[0]["attributes"][0]["value"], "Red")
        self.assertEqual(response.data[0]["attributes"][1]["attribute"], "Size")
        self.assertEqual(response.data[0]["attributes"][1]["value"], "Medium")

    def test_filter_products_by_attribute_value(self):
        response = self.client.get(
            "/api/products/", {"productattributevalue__value": "Red"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Product 1")
        self.assertEqual(response.data[0]["attributes"][0]["value"], "Red")
