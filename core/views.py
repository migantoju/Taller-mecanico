from django.shortcuts import render, get_object_or_404, redirect
from .models import (Cliente,
                    Vehiculo,
                    Mecanico_Responsable,
                    Responsable,
                    HojaParte,
                    Repuesto, 
                    Factura)
from django.contrib.auth.decorators import login_required
from .forms import RegistrarClienteForm, RegistrarVehiculo, RegistrarMecanicoResponsableForm
# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

@login_required
def registrar_cliente(request):
    if request.method == 'POST':
        form = RegistrarClienteForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.save()
            return redirect('/taller/clientes/')
    else:
        form = RegistrarClienteForm()
    return render(request, 'core/nuevo_cliente.html', {'form':form, 'section':'nuevo'})

@login_required
def clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'core/clientes.html', {'clientes':clientes, 'section':'clientes'})

@login_required
def detalle_cliente(request, pk=None):
    cliente = get_object_or_404(Cliente, pk=pk)
    vehiculo = Vehiculo.objects.filter(cliente_vehiculo=cliente)
    responsable = Responsable.objects.filter(vehiculo=vehiculo)
    return render(request, 'core/detalle_cliente.html', {'cliente':cliente, 'vehiculo':vehiculo, 'responsable':responsable})

@login_required
def registrar_vehiculo(request):
    if request.method == 'POST':
        form = RegistrarVehiculo(request.POST or None)
        if form.is_valid():
            v = form.save(commit=False)
            v.user = request.user
            v.save()
            return redirect('/taller/clientes/')
    else:
        form = RegistrarVehiculo()
    return render(request, 'core/registrar_vehiculo.html', {'form':form, 'section':'nuevov'})

@login_required
def mecanico_responsable(request):
    if request.method == 'POST':
        form = RegistrarMecanicoResponsableForm(request.POST or None)
        if form.is_valid():
            responsable = form.save(commit=False)
            responsable.user = request.user
            responsable.save()
            return redirect('/taller/clientes/')
    else:
        form = RegistrarMecanicoResponsableForm()
    return render(request, 'core/nuevo_mecanico_responsable.html', {'form':form, 'section':'nuevom'})