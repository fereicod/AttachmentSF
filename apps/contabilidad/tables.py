# App Extension
import django_tables2 as tables

# Custom
from .models import Att,Provision

class AttTable(tables.Table):
    ''' Creamos el la tabla con el modelo Attachment '''
    class Meta:
        model = Att

class ProvisionTable(tables.Table):
    ''' Creamos el la tabla con el modelo Provision '''
    class Meta:
        model = Provision
