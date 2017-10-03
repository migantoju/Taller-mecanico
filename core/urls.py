from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevo/$', views.registrar_cliente, name='nuevo_cliente'),
    url(r'^clientes/$', views.clientes, name='clientes'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.detalle_cliente, name='detalle_cliente'),
    url(r'^nuevo/vehiculo/$', views.registrar_vehiculo, name='nuevo_vehiculo'),
    url(r'^nuevo/mecanico/$', views.mecanico_responsable, name='nuevo_mecanico'),
]