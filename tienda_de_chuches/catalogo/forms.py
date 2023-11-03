from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Foto,Facturacion


class NewRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username', 
        max_length=250, 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}),
        help_text="Este campo es obligatorio."
    )

    first_name = forms.CharField(
        label='Nombre', 
        max_length=250, 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Nombre'}),
        help_text="Este campo es obligatorio."
    )
    
    last_name = forms.CharField(
        label='Apellidos', 
        max_length=250, 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Apellido'}),
        help_text="Este campo es obligatorio."
    )
    
    email = forms.EmailField(
        label='Email', 
        max_length=250, 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Email'}),
        help_text="Este campo es obligatorio."
    )
    
    telefono = forms.CharField(
        label='Telefono', 
        max_length=15,
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Telefono'}),
        help_text="Este campo es obligatorio."
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Contraseña'}),
        help_text="La contraseña debe tener al menos 8 caracteres y contener al menos una letra mayúscula, una letra minúscula, y un número."
    )
    
    password2 = forms.CharField(
        label='Repetir contraseña', 
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Repetir contraseña'}),
        help_text="Repite la contraseña."
    )
    
    direccion = forms.CharField(
        label='Direccion',
        max_length=250,
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Direccion'}),
        help_text="Este campo es obligatorio."
    )
    
    ciudad = forms.CharField(
        label='Ciudad',
        max_length=250,
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Ciudad'}),
        help_text="Este campo es obligatorio."
    )
    
    codigo_postal = forms.CharField(
        label='Codigo postal',
        max_length=250,
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Codigo postal'}),
        help_text="Este campo es obligatorio."
    )

    usuario_premium = forms.BooleanField(
        label='¿Quieres ser usuario premium? ',
        required=False,
        widget=forms.CheckboxInput(attrs={'class':"form-control",'placeholder':'Usuario premium'})
    )


    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)  
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
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




