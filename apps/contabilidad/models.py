from django.db import models

# Create your models here.
class Provision(models.Model):
    ''' Modelo de Provision, el cual solo contendra valores referenciados desde Salesforce '''

    idSF = models.CharField(max_length=255)
    name = models.CharField(max_length=20, primary_key = True)
    estatus = models.CharField(max_length=20)
    ejecucionPago = models.CharField(max_length=20)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

class AttIndex(models.Model):
    ''' Modelo para la captura de la información de los archivos adjuntos '''

    att_index_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

class Att(models.Model):
    ''' Modelo de Attachment, el cual solo contendra valores referenciados desde Salesforce, con su padre [Provision] '''

    att_pk = models.AutoField(primary_key=True)
    provision = models.ForeignKey(Provision,blank=True, null=True)
    name = models.CharField(max_length=255)
    index = models.FileField(
        upload_to='contabilidad.AttIndex/bytes/filename/mimetype',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.name


    



