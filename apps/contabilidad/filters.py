# App Extension
from django_filters import FilterSet

# Custom
from .models import Att, Provision

class AttFilter(FilterSet):
    ''' Creamos el tipo de filtro que queremos obtener '''
    class Meta:
        model = Att
        fields = {
            'name': ['exact', 'contains'],
        }

class ProvisionFilter(FilterSet):
    ''' Creamos el tipo de filtro que queremos obtener '''
    class Meta:
        model = Provision
        fields = {
            'name': ['exact', 'contains'],
        }