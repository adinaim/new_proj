from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.utils.decorators import method_decorator  # cashing
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from .serializers import (
    ProductListSerailizer, 
    ProductSerializer, 
    CategorySerializer
    )

from .models import Category, Product, ProductImage


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    
    # def get_queryset(self):
    #     return Product.objects.all()

    @method_decorator(cache_page(60*15))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerailizer
        return ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        instance: Product = self.get_object() # Product model
        instance.views_count += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer