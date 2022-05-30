from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
from .logistic_filters import StockFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = StockFilter
