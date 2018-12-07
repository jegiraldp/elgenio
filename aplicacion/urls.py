from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/listar', views.getclientes, name='getclientes')
]