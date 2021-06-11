import django_filters

from .models import Company_Data
import django_filters

class Company_DataFilter(django_filters.FilterSet):
    class Meta:
        model = Company_Data
        fields = '__all__'