# Django
from django.conf.urls import url, include

# Custom 
from .views import migrate, MultipleTables

urlpatterns = [
    url(r'^migrate/$', migrate, name='migrate'),
    url(r'^multiple/$', MultipleTables.as_view(), name='multitableview'),
]
