from django.contrib import admin
from .models import (Cliente,
                    Vehiculo,
                    Mecanico_Responsable,
                    Responsable,
                    HojaParte,
                    Repuesto, 
                    Factura)
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Mecanico_Responsable)
admin.site.register(Responsable)
admin.site.register(HojaParte)
admin.site.register(Repuesto)
admin.site.register(Factura)