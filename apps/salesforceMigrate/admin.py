# Django
from django.contrib import admin

# App django-salesforce
from apps.salesforceMigrate import models

class ProvisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'estatus',)

admin.site.register(models.Provision, ProvisionAdmin)

class EjecucionPagoAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Ejecuci_n_Pago, EjecucionPagoAdmin)

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Attachment, AttachmentAdmin)