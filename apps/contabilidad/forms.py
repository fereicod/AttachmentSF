# django
from django import forms
from django.contrib.admin.forms import forms as adminforms
# third party
from db_file_storage.form_widgets import DBClearableFileInput, \
    DBAdminClearableFileInput
# project
from .models import Att

class AttForm(forms.ModelForm):
    class Meta(object):
        model = Att
        exclude = []
        widgets = {
            'index': DBClearableFileInput,
        }

class AttAdminForm(adminforms.ModelForm):
    class Meta(object):
        model = Att
        exclude = []
        widgets = {
            'index': DBAdminClearableFileInput,
        }
