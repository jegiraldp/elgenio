from django.shortcuts import render
from .models import cliente

def index(request):
    ctx={'info':'-- Sistema de Información -- '}
    return render (request,"aplicacion/inicio.html",ctx)

def getclientes(request):
    lista = cliente.objects.order_by('nombreE')
    ctx = {'clientes': lista}
    return render(request, "aplicacion/listadoClientes.html", ctx)
