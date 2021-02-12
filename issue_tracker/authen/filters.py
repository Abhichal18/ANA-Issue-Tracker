import django_filters
from django_filters import CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    question=CharFilter(field_name='question', lookup_expr='icontains')
    class Meta:
        model = questions
        fields = '__all__'
        exclude=['answer']
