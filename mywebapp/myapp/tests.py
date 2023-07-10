from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):
    def test_product_creation(self):
        # Create a new product and save it to the database
        Product.objects.create(name='Test Product', description='This is a test product', price=9.99)

        # Retrieve the product from the database
        product = Product.objects.get(name='Test Product')

        # Check if the product was created correctly
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.price, 9.99)


class ProductViewTest(TestCase):
    def test_product_list_view(self):
        # Send a GET request to the product list view
        response = self.client.get('/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        # Create a new product and save it to the database
        product = Product.objects.create(name='Test Product', description='This is a test product', price=9.99)

        # Send a GET request to the product detail view with the product's primary key (pk)
        response = self.client.get(f'/product/{product.pk}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
