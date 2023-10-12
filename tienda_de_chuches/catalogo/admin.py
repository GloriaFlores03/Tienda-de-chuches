from django.contrib import admin
from .models import Cliente,Empleado,Producto,Foto
from django.contrib.auth.models import Permission

admin.site.register(Permission)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Foto)
# Register your models here.
