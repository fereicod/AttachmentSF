# App Extension
import django_tables2 as tables

# Custom 
from .models import Provision

class ProvisionTable(tables.Table):
    ''' Creamos la estructura de la tabla de acuerdo al modelo Provision '''
    name = tables.Column()
    class Meta:
        model = Provision
