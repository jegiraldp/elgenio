from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.getclientes, name='getclientes'),
    path('servicios/', views.getservicios, name='getservicios')
]