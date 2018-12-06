from django.shortcuts import render

def index(request):
    ctx={'info':'-- Sistema de Información -- Extintores EL GENIO '}
    return render (request,"aplicacion/inicio.html",ctx)
