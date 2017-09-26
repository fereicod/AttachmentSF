# App Django-salesforce
from salesforce import models
from salesforce.models import SalesforceModel as SalesforceModelParent

# Django
import django
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

# This class customizes `managed = True` for tests and does not disturbe SF
class SalesforceModel(SalesforceModelParent):
    class Meta:
        abstract = True
        managed = True

class SalesforceParentModel(SalesforceModel):
    """
    Example of standard fields present in all custom models.
    """
    # This is not a custom field because is not defined in a custom model.
    # The API name is therefore 'Name'.
    name = models.CharField('# Provisión',max_length=80)
    last_modified_date = models.DateTimeField(sf_read_only=models.READ_ONLY)
    # This model is not custom because it has not an explicit attribute
    # `custom = True` in Meta and also has not a `db_table` that ends with
    # '__c'.

    class Meta:
        abstract = True

class Ejecuci_n_Pago(SalesforceParentModel):
    ''' Creamos el modelo de Ejecucion de Pago de acuerdo como esta en Salesforce '''
    class Meta:
        custom = True
        db_table = 'Ejecuci_n_Pago__c'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Provision(SalesforceParentModel):
    ''' Creamos el modelo de Provision de acuerdo como esta en Salesforce '''
    estatus = models.CharField(max_length=20)
    Ejecuci_n_Relacionada = models.ForeignKey(Ejecuci_n_Pago,on_delete=models.DO_NOTHING, blank=True, null=True)

    #fecha_de_factura = models.CharField('Fecha de Factura', max_length=15,db_column='Fecha_de_Factura__c')
    #caja_Chica_Relacionada = models.CharField('Caja Chica Relacionada',db_column='Caja_Chica_Relacionada__c',max_length=255)

    class Meta:
        custom = True
        db_table = 'Provision__c'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Attachment(models.Model):
    ''' Creamos el modelo de Attachment de acuerdo como esta en Salesforce '''
    # A standard SFDC object that can have a relationship to any custom object
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Provision, sf_read_only=models.NOT_UPDATEABLE, on_delete=models.DO_NOTHING)
    # The "body" of Attachment can't be queried for more rows togehter.
    body = models.TextField()

#class Test(SalesforceParentModel):
#    """
#    Simple custom model with one custom and more standard fields.
#
#    Salesforce object for this model can be created:
#    A) automatically from the branch hynekcer/tooling-api-and-metadata
#       by commands:
#        $ python manage.py shell
#            >> from salesforce.backend import tooling
#            >> tooling.install_metadata_service()
#            >> tooling.create_demo_test_object()
#    or
#    B) manually can create the same object with `API Name`: `django_Test__c`
#        `Data Type` of the Record Name: `Text`
#
#       Create three fields:
#       Type            | API Name | Label
#       ----------------+----------+----------
#       Text            | TestText | Test Text
#       Checkbox        | TestBool | Test Bool
#       Lookup(Contact) | Contact  | Contact
#
#       Set it accessible by you. (`Set Field-Leved Security`)
#    """
#    # This is a custom field because it is defined in the custom model.
#    # The API name is therefore 'TestField__c'
#    test_text = models.CharField(max_length=40)
#    test_bool = models.BooleanField(default=False)
#    #contact = models.ForeignKey(Contact, null=True, on_delete=models.DO_NOTHING)
#
#    class Meta:
#        custom = True
#        db_table = 'django_Test__c'

