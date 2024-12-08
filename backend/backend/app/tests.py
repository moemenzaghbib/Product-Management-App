from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductAPITestCase(APITestCase):

    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'description': 'A test product',
            'price': 100.0,
            'stock': 10
        }
        self.product = Product.objects.create(**self.product_data)

    def test_product_list(self):
        url = '/api/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.product.name)
        self.assertEqual(response.data[0]['stock'], self.product.stock)

    def test_product_detail(self):
        url = f'/api/products/{self.product.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(response.data['stock'], self.product.stock)

    def test_create_product_valid(self):
        url = '/api/products/'
        valid_data = {
            'name': 'New Product',
            'description': 'A new test product',
            'price': 150.0,
            'stock': 20
        }
        response = self.client.post(url, valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], valid_data['name'])
        self.assertEqual(response.data['stock'], valid_data['stock'])

    def test_create_product_invalid(self):
        url = '/api/products/'
        invalid_data = {
            'name': '',
            'description': 'A new product',
            'price': 150.0,
            'stock': 20
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_update_product_valid(self):
        url = f'/api/products/{self.product.id}/'
        updated_data = {
            'name': 'Updated Product',
            'description': 'An updated test product',
            'price': 120.0,
            'stock': 25
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])
        self.assertEqual(response.data['stock'], updated_data['stock'])

    def test_update_product_invalid(self):
        url = f'/api/products/{self.product.id}/'
        invalid_data = {
            'name': '',
            'description': 'An updated test product',
            'price': 120.0,
            'stock': 25
        }
        response = self.client.put(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_partial_update_product(self):
        url = f'/api/products/{self.product.id}/'
        partial_data = {
            'price': 110.0
        }
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price'], partial_data['price'])

    def test_delete_product(self):
        url = f'/api/products/{self.product.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_product_list_empty(self):
        Product.objects.all().delete()
        url = '/api/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_invalid_product_id(self):
        url = '/api/products/9999/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_create_product(self):
        url = '/api/products/'
        invalid_data = {
            'description': 'A new product with missing name and price',
            'stock': 5
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('price', response.data)
