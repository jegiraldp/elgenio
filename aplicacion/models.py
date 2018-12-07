from django.db import models
from datetime import datetime

class cliente(models.Model):
    nit = models.CharField(max_length=30, null=False, blank=False, default='0')
    Nombre = models.CharField(max_length=50, null=False, blank=False)
    Direccion =models.CharField(max_length=50, null=False, blank=False)
    Telefono =models.CharField(max_length=50,  null=False, blank=False)
    Descripcion=models.CharField(max_length=100,  null=True, blank=False)

    def __str__(self):
        return self.Nombre

class servicio(models.Model):
    idS = models.AutoField(primary_key=True)
    Fecha = models.DateField(default=datetime.now)
    Cliente = models.ForeignKey(cliente, null=False, blank=False,on_delete=models.CASCADE)
    ls=(('Venta','Venta'),('Recarga','Recarga'),('Reparación','Reparación'))
    Cantidad = models.IntegerField(null=False, blank=False)
    Servicio = models.CharField(max_length=20, choices=ls, default='01')

    def __str__(self):
        return self.Cliente.Nombre+" ("+self.Servicio+" el "+str(self.Fecha)+")"


