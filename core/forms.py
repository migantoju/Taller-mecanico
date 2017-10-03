from django import forms
from .models import (Cliente,
                    Vehiculo,
                    Mecanico_Responsable,
                    Responsable,
                    HojaParte,
                    Repuesto, 
                    Factura)

class RegistrarClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'direccion_cliente', 'telefono_cliente', )

    def __init__(self, *args, **kwargs):
        super(RegistrarClienteForm, self).__init__(*args, **kwargs)
        self.fields['nombre_cliente'].required = True
        self.fields['direccion_cliente'].required = True
        self.fields['telefono_cliente'].required = True

class RegistrarVehiculo(forms.ModelForm):
    cliente_vehiculo = forms.SelectMultiple()
    class Meta:
        model = Vehiculo
        fields = ('matricula', 'modelo_vehiculo', 'color_vehiculo', 'cliente_vehiculo', )

    def __init__(self, *args, **kwargs):
        super(RegistrarVehiculo, self).__init__(*args, **kwargs)
        self.fields['matricula'].required = True
        self.fields['modelo_vehiculo'].required = True
        self.fields['color_vehiculo'].required = True
        self.fields['cliente_vehiculo'].required = True

class RegistrarMecanicoResponsableForm(forms.ModelForm):

    class Meta:
        model = Mecanico_Responsable
        fields = ('nombre_mecanico', 'direccion_mecanico', 'telefono_mecanico', 'cost_x_hora', )
    
    def __init__(self, *args, **kwargs):
        super(RegistrarMecanicoResponsableForm, self).__init__(*args, **kwargs)
        self.fields['cost_x_hora'].required = True 
        self.fields['direccion_mecanico'].required = True 
        self.fields['telefono_mecanico'].required = True 
        self.fields['nombre_mecanico'].required = True 
        self.fields['cost_x_hora'].widget.attrs['placeholder'] = '185.20'
