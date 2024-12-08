from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']
        extra_kwargs = {
            'price': {'min_value': 0},
            'stock': {'min_value': 0}
        }
