from django.db import models

class cliente(models.Model):
    nitE = models.CharField(max_length=30, null=False, blank=False, default='0')
    nombreE = models.CharField(max_length=50, null=False, blank=False)
    direccionE=models.CharField(max_length=50, null=False, blank=False)
    telefonoE=models.CharField(max_length=50,  null=False, blank=False)
    descripcionE=models.CharField(max_length=100,  null=True, blank=False)

    def __str__(self):
        return self.nombreE + " - ("+self.telefonoE+")"





