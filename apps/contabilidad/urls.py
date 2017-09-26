# Django
from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Custom
from .forms import AttForm
from .models import Att
from .views import FilteredAttListView

urlpatterns = [
    url(r'^filter/$', FilteredAttListView.as_view(), name='FilterAtt'),
    url(
        r'^att/add/$',
        CreateView.as_view(
            model=Att,
            form_class=AttForm,
            template_name='att_form.html',
            success_url=reverse_lazy('contabilidad:conta')
            
        ),
        name='attAdd'
    ),
]
