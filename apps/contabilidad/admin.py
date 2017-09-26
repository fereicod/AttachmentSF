from django.contrib import admin

# Register your models here.
from .forms import AttAdminForm
from .models import Att, Provision

class AttAdmin(admin.ModelAdmin):
    form = AttAdminForm

admin.site.register(Att, AttAdmin)

class ProvisionAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Provision, ProvisionAdmin)   