from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.routers import DefaultRouter
from django.urls import reverse
from django.urls import path, include
from app.views import ProductViewSet  # Replace `app` with your actual app name

# Define the router and register your viewset
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': {
            'list': request.build_absolute_uri(reverse('product-list')),
            'create': request.build_absolute_uri(reverse('product-list')),
            'retrieve': '/products/<id>/ (GET)',
            'update': '/products/<id>/ (PUT)',
            'partial_update': '/products/<id>/ (PATCH)',
            'delete': '/products/<id>/ (DELETE)',
            'in_stock': request.build_absolute_uri(reverse('product-in-stock')),
        },
    })

urlpatterns = [
    path('', api_root),  
    path('api/', include(router.urls)),  
]
