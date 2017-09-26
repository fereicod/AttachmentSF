# Django
from django.shortcuts import render

# App Extension
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2 import SingleTableView

# Custom
from .tables import AttTable, ProvisionTable
from .models import Att, Provision
from .filters import AttFilter, ProvisionFilter

class FilteredAttListView(FilterView, ExportMixin, SingleTableView):
    ''' Establece una tabla con el objeto / modelo Attachment, asi mismo definiendo su plantilla. Por último 
        se carga el tipo de filtro a buscar de acuerdo a su modelo. '''
    print(".........................")
    table_class = AttTable
    table_class = AttTable
    model = Att
    template_name = 'filter.html'
    filterset_class = AttFilter

class FilteredProvisionListView(FilterView, ExportMixin, SingleTableView):
    ''' Establece una tabla con el objeto / modelo Provision, asi mismo definiendo su plantilla. Por último
        se carga el tipo de filtro a buscar de acuerdo a su modelo. '''
    table_class = ProvisionTable
    model = Provision
    template_name = 'filter.html'
    filterset_class = ProvisionFilter