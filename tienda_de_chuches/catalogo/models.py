from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User


class Cliente(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    telefono = models.CharField(max_length=15)
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
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    entrega=models.CharField(max_length=1000)
    precio=models.DecimalField(max_digits=6,decimal_places=2,blank=True, null=True)

    def __str__(self):
        return self.entrega
    

class Facturacion(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)

    numero_tarjeta = models.CharField(max_length=16)
    vencimiento_tarjeta = models.DateField()
    cvv_tarjeta = models.CharField(max_length=4)


    def calcular_total(self):
        total = 0
        for item in self.carrito.itemcarrito_set.all():
            total += item.cantidad * item.producto.costo_producto

        # Busca el medio de entrega del cliente actual
        medio_entrega = MedioEntrega.objects.get(cliente=self.cliente)
        
        # Suma el precio del medio de entrega al total
        total += medio_entrega.precio

        return total

    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Facturacion #{self.id} - Cliente: {self.cliente.id_user.username}"



