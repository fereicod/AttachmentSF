from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.usuario.views import (
	#RegistroUsuario, 
	UserAPI,
	home
)

urlpatterns = [
	url(r'^$', login_required(home), name='home'),
	#url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	url(r'^api', UserAPI.as_view(), name="api"),

]
