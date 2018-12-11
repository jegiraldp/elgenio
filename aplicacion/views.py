from django.shortcuts import render
from .models import cliente, servicio

def index(request):
    ctx={'info':' -- Extintores EL GENIO -- '}
    return render (request,"aplicacion/inicio.html",ctx)

def getclientes(request):
    lista = cliente.objects.order_by('Nombre')
    ctx = {'clientes': lista}
    return render(request, "aplicacion/listadoClientes.html", ctx)

def getservicios(request):
    lista = servicio.objects.order_by('Fecha')
    ctx = {'servicios': lista}
    return render(request, "aplicacion/listadoServicios.html", ctx)
