from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 


class Cliente(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    codigo_postal=models.CharField(max_length=250)
    usuario_premium = models.BooleanField(default=False)


    class Meta: 
        ordering = ['id_user']

    def __str__(self):
        return f"{self.id_user}"


class Empleado(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    codigo_postal=models.CharField(max_length=250)


    class Meta:
        ordering = ['id_user']

    def __str__(self):
        return f"{self.id_user}"


class Producto(models.Model):
    nombre_producto=models.CharField(max_length=250)
    descripcion_producto=models.TextField(max_length=600)  # Genera opciones del 1 al 10
    sabores = models.CharField(max_length=250)
    costo_producto=models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return self.nombre_producto

class Foto(models.Model):
    id_producto=models.ForeignKey('Producto',on_delete=models.SET_NULL,null=True)
    subir_foto_p=models.ImageField(upload_to="fotos_de_productos",null=True)


    class Meta:
        ordering=['id_producto']

    def get_absolute_url(self):
        return reverse('foto', args=[str(self.id)])

    def __str__(self):
        return f"{self.id_producto}"


class Carrito(models.Model):
    cliente =models.ForeignKey('Cliente', on_delete=models.CASCADE)
    productos=models.ManyToManyField(Producto,through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.cliente.user.username}"

class ItemCarrito(models.Model):
    carrito=models.ForeignKey('Carrito',on_delete=models.CASCADE)
    producto=models.ForeignKey('Producto',on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre_producto}"
    
class MedioEntrega(models.Model):
    entrega=models.CharField(max_length=1000)#regoer en tienda o a domicilio
    precio=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.entrega
    

class Facturacion(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.CharField(max_length=300)  # Agrega dirección de envío
    ciudad_envio = models.CharField(max_length=250)     # Agrega ciudad de envío
    total = models.DecimalField(max_digits=10, decimal_places=2)
    medio_entrega = models.ForeignKey('MedioEntrega', on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16)


    def calcular_total(self):
        # Calcula el total teniendo en cuenta la cantidad, precio y costo de envío
        total = 0
        for item in self.carrito.itemcarrito_set.all():
            total += item.cantidad * item.producto.costo_producto
        total += self.medio_entrega.precio  # Agrega costo de envío
        return total

    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Facturacion #{self.id} - Cliente: {self.cliente.id_user.username}"# Create your models here.
