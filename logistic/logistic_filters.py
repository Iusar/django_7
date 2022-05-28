import django_filters
from .models import StockProduct, Stock


class StockFilter(django_filters.FilterSet):

    class Meta:
        model = Stock
        fields = ['address', 'products']
