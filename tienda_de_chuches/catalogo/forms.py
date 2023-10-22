from django import forms
#from creditcard.forms import CardNumberField, CardExpiryField, SecurityCodeField
from django.core.exceptions import ValidationError


from django.contrib.auth.forms import UserCreationForm
from .models import Foto,Facturacion
class NewRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))

    first_name = forms.CharField(label='Nombre', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Nombre'}))
    
    last_name = forms.CharField(label='Apellidos', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Apellido'}))
    
    email = forms.EmailField(label='Email', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Email'}))
    
    telefono = forms.CharField(label='Telefono', max_length=15,
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Telefono'}))
    
    password1 = forms.CharField(label='password',
                    widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Contraseña'}))
    
    password2 = forms.CharField(label='repeat password', 
                    widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'repite la contraseña'}))
    
    direccion= forms.CharField(label='Direccion',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Direccion'}))
    
    ciudad = forms.CharField(label='Ciudad',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Ciudad'}))
    
    codigo_postal = forms.CharField(label='Codigo postal',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Codigo postal'}))

    usuario_premium = forms.BooleanField(label='¿Quieres ser usuario premium? ',required=False,
                        widget=forms.CheckboxInput(attrs={'class':"form-control",'placeholder':'Usuario premium'}))

class EditPerfilForm(forms.Form):
    first_name=forms.CharField(label='Nombre',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'nombre'}))
    
    last_name=forms.CharField(label='Apellido',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'apellidos'}))
    
    email = forms.EmailField(label='Email',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'email'}))
    
    telefono = forms.CharField(label='Telefono', max_length=15,
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Telefono'}))
    
    direccion= forms.CharField(label='Direccion',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Direccion'}))
    
    ciudad = forms.CharField(label='Ciudad',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Ciudad'}))
    
    codigo_postal = forms.CharField(label='Codigo postal',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Codigo postal'}))


class NewProductoForm(forms.Form):
    nombre_producto=forms.CharField(label='Nombre del producto', max_length=250,
                    widget=forms.Textarea(attrs={'class':"form-control",'placeholder':'nombre del producto'}))
    
    descripcion_producto=forms.CharField(label='Descripcion del producto',max_length=500,
                    widget=forms.Textarea(attrs={'class':"form-control",'placeholder':'descripcion del producto'}))
    
    sabores = forms.CharField(label='Sabores',max_length=500,
                    widget=forms.Textarea(attrs={'class':"form-control",'placeholder':'sabores'}))
    
    costo_producto = forms.DecimalField(label='Costo producto',max_digits=10,decimal_places=2,
                        widget=forms.NumberInput(attrs={'class':"form-control",'placeholder':'costo del producto'}))
    

class SubirFoto(forms.ModelForm):
    class Meta:
        model=Foto
        fields=['id_producto','subir_foto_p']


class FacturacionForm(forms.ModelForm):
    class Meta:
        model = Facturacion  # Asocia el formulario al modelo Facturacion
        fields = ['numero_tarjeta', 'vencimiento_tarjeta', 'cvv_tarjeta']
        labels = {
            'numero_tarjeta': 'Número de Tarjeta',
            'vencimiento_tarjeta': 'Fecha de Vencimiento',
            'cvv_tarjeta': 'CVV de la Tarjeta'
        }

    vencimiento_tarjeta = forms.DateField(
        label='Fecha de Vencimiento',
        widget=forms.SelectDateWidget()  # Utiliza el widget SelectDateWidget
    )




