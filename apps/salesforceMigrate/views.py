# Django
from django.db import connections
from django.shortcuts import redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.generic.base import TemplateView

# App Extension
from salesforce.backend.driver import handle_api_exceptions 
from django_tables2 import MultiTableMixin                  

# Custom
from apps.salesforceMigrate.models import Provision as sfProv, Attachment
from apps.contabilidad.models import Provision as cProv, Att
from .tables import ProvisionTable

# Filter Provision for 'estatus'
estatus_op = ['Contabilizada', 'Programada', 'Pagada']

# Querys
qs = sfProv.objects.filter(estatus__in=estatus_op)  # Salesforce Model
qs2 = cProv.objects.filter(estatus__in=estatus_op)  # Contabilidad Model

class MultipleTables(MultiTableMixin, TemplateView):
    ''' Clase que define las consultas y las muestra en una sola pagina; con el plugin django_tables2 '''

    template_name = 'multiTable.html'
    tables = [
        ProvisionTable(qs, exclude=('id','last_modified_date', )),
        ProvisionTable(qs2, exclude=('id','last_modified_date', ))
    ]

    table_pagination = {
        'per_page': 20
    }

def migrate(request):
    ''' Proceso de Migracion a la DB "Contabilidad". Valida si ya existio previamente una provision, de ser así,
        solo lo va actualizar. Para ambos casos consulta los attachments y los inserta.
    '''
    for p in qs:
        #print(str(p))
        try:
            print("===================>   Vamos a insertar   <================")
            cProv.objects.create(idSF=str(p.id),name=str(p), estatus=str(p.estatus), ejecucionPago=str(p.Ejecuci_n_Relacionada)).save()
            print(p.id+ ' | ' +p+ ' | ' +p.estatus+ ' | ' +p.Ejecuci_n_Relacionada)
            saveAtt(p.id, p)
        except:
            print('Error al repetir numero')
            print("===================>   Vamos a actualizar   <================")
            pcr = cProv.objects.get(name=str(p))
            pcr.idSF = str(p.id)
            pcr.estatus = str(p.estatus)
            pcr.ejecucionPago = str(p.Ejecuci_n_Relacionada)
            pcr.save()
            print(pcr.idSF+ ' | ' +pcr.name+ ' | ' +pcr.estatus+ ' | ' +pcr.ejecucionPago)
            saveAtt(pcr.idSF, pcr.name)
            
    return redirect('salesforceMigrate:multitableview')

def saveAtt(idProv, nameProv):
    ''' Funcion para insertar los Attachments con su respectivo Provision relacionada. '''

    # Hacemos conexion con Saleforce por medio de session, y consultar el contenido de cada archivo adjunto
    session = connections['salesforce'].sf_session
    attch = Attachment.objects.filter(parent=idProv)
    for a in attch:
        url = session.auth.instance_url + a.body
        blob2 = handle_api_exceptions(url, session.get)._content
        file = SimpleUploadedFile(a.name, blob2)
        try:
            #Si ya existe el archivo adjunto, no volveremos a cargarlo
            adj = Att.objects.filter(provision=str(nameProv),name=a.name)

            if not (adj.count()):
                print("===================> Create Attachment of " + nameProv + " <================")
                print("Atta => "+a.name)
                Att.objects.create(name=a.name, index=file, provision_id=str(nameProv))

            #else:
                #print("===================>  Update Attachment of " + nameProv + " <================")
                #for a in adj:
                #    a.index = file
                #    a.provision = str(nameP)
                #print(adj)

        except:
            print('============ Error Save / Update Attachment(s); Provision: '+nameProv)

