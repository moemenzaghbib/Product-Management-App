from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.core.paginator import Paginator 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        products = Product.objects.filter(stock__gt=0)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        
        
        
    @action(detail=False, methods=['get'], url_path='paginated-products')
    def paginated_products(self, request):
        page_size = int(request.GET.get('page_size', 5))  # Default page size 5
        page_number = int(request.GET.get('page', 1))  # Default page number 1
        in_stock = request.GET.get('in_stock', 'false').lower() == 'true'

        products = Product.objects.all()
        if in_stock:
            products = products.filter(stock__gt=0)

        paginator = Paginator(products, page_size)
        try:
            current_page = paginator.page(page_number)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        serializer = ProductSerializer(current_page.object_list, many=True)
        return Response({
            'data': serializer.data,
            'has_more': current_page.has_next(),
            'current_page': page_number,
            'total_pages': paginator.num_pages
        })
