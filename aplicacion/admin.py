from django.contrib import admin
from .models import cliente, servicio, remision


##########cliente


class clienteAdmin(admin.ModelAdmin):
    empty_value_display = '-no-'
    fields = ('Nombre', 'Direccion', 'Telefono','Descripcion')
    exclude = ('nit',)
    list_display = ('Nombre', 'Direccion', 'Telefono','Descripcion')

admin.site.register(cliente,clienteAdmin)


###
#######servicio
class servicioAdmin(admin.ModelAdmin):
    empty_value_display = '-no-'
    fields = ('Fecha', 'Cliente', 'Cantidad','Servicio','Comentario')
    #exclude = ('nit',)
    list_display = ('Fecha', 'Cliente', 'Cantidad','Servicio','Comentario')
    date_hierarchy = 'Fecha'
    #servicio.admin_order_field='Fecha'
    #list_display_links = ('Cliente', 'Fecha')
    list_filter = ('Servicio','Fecha')
    list_per_page = 5
    search_fields = ['Cliente__Nombre',]
    save_on_top = True

admin.site.register(servicio,servicioAdmin)
##
#######remision
class remisionAdmin(admin.ModelAdmin):
    empty_value_display = '-no-'
    fields = ('Fecha', 'Cantidad','Comentario')
    list_display = ('Fecha', 'Cantidad','Comentario')
    list_filter = ('Fecha',)
    date_hierarchy = 'Fecha'
    save_on_top = True
    list_per_page = 5

#admin.site.register(remision,remisionAdmin)