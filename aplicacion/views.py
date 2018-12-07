from django.shortcuts import render
from .models import cliente, servicio

def index(request):
    ctx={'info':'-- Sistema de Información -- '}
    return render (request,"aplicacion/inicio.html",ctx)

def getclientes(request):
    lista = cliente.objects.order_by('Nombre')
    ctx = {'clientes': lista}
    return render(request, "aplicacion/listadoClientes.html", ctx)

def getservicios(request):
    lista = servicio.objects.order_by('Cliente')
    ctx = {'servicios': lista}
    return render(request, "aplicacion/listadoServicios.html", ctx)
