from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth import login as auth_login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import NewRegisterForm,EditPerfilForm,NewProductoForm,SubirFoto
from .models import Cliente,Empleado,Producto,Foto,Carrito,ItemCarrito
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def register(request):
    message = 0
    if request.method =='POST':
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()

                registers=Cliente.objects.create(
                    id_user=user,
                    telefono=form.cleaned_data['telefono'],
                    direccion=form.cleaned_data['direccion'],
                    ciudad=form.cleaned_data['ciudad'],
                    codigo_postal=form.cleaned_data['codigo_postal'],
                    usuario_premium = form.cleaned_data['usuario_premium']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.save()

                message = 1
                form = NewRegisterForm()
            
            except:
                    message = 3
        else:
            message = 2
    else:
        form = NewRegisterForm()

    context = {
        'form': form,
        'message': message,
    
    }

    return render(request, "register.html", context=context)


def login(request):
    if request.method=='POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('profile_cliente')
    else:
        form=AuthenticationForm()

    context={
        'form':form,
    }

    return render(request,'login.html',context=context)


def profile_cliente(request):
    if request.user.is_authenticated:
        user=request.user
        registers=Cliente.objects.get(id_user=user)

    context={
        'user':user,
        'registers':registers,
    }

    return render(request,'profile_cliente.html',context=context)


@login_required
def edit_profile_cliente(request):
    message = 0
    user = request.user
    cliente = None  # Declarar la variable cliente antes de usarla

    if request.method == 'POST':
        form = EditPerfilForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            # Utiliza get_or_create para obtener o crear un objeto Cliente relacionado con el usuario
            cliente, created = Cliente.objects.get_or_create(id_user=user)

            # Actualiza los campos del cliente
            cliente.telefono = form.cleaned_data['telefono']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.ciudad = form.cleaned_data['ciudad']
            cliente.codigo_postal = form.cleaned_data['codigo_postal']
            cliente.save()

            message = 1

    else:
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }

        # Intenta obtener un objeto Cliente relacionado con el usuario
        cliente = Cliente.objects.filter(id_user=user).first()

        if cliente:
            initial_data['telefono'] = cliente.telefono
            initial_data['direccion'] = cliente.direccion
            initial_data['ciudad'] = cliente.ciudad
            initial_data['codigo_postal'] = cliente.codigo_postal

        form = EditPerfilForm(initial=initial_data)

    context = {
        'form': form,
        'message': message,
    }

    return render(request, 'edit_profile_cliente.html', context=context)

@login_required
def profile_empleado(request):
    if request.user.is_authenticated:
        user=request.user
        empleado=Empleado.objects.get(id_user=user)
    
    context={
        'empleado':empleado,
    }
    return render(request,'profile_empleado.html',context=context)

@login_required
def new_producto(request):
    message=0
    if request.method=='POST':
        form=NewProductoForm(request.POST)
        if form.is_valid():
            try:
                producto=Producto()
                producto.nombre_producto=form.cleaned_data['nombre_producto']
                producto.descripcion_producto=form.cleaned_data['descripcion_producto']
                producto.sabores = form.cleaned_data['sabores']
                producto.costo_producto = form.cleaned_data['costo_producto']
                producto.save()

                message=1
                form=NewProductoForm()
            except:
                message=3
        else:
            message=2
    else:
        form=NewProductoForm()

    context = {
        'form':form,
        'message':message,
    }

    return render (request,'new_producto.html',context=context)

@login_required
def subir_foto_p(request,pk):

    message=""
    if request.method=='POST':
        form=SubirFoto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message=1
    else:
        form=SubirFoto()
    
    context={
        'message':message,
        'form':form,
    }

    return render(request, 'subir_foto_p.html',context)

def productos(request):
    productos_lista=Producto.objects.all()
    context={
        'productos_lista':productos_lista,
    }
    return render(request,"productos.html",context=context)


def productos_detalles(request,id):
    productos_detalles=Producto.objects.get(id=id)
    foto_lista= Foto.objects.filter(id_producto=id)

    if request.method =='POST':
        request.session['producto unitario'] = productos_detalles.id

    context={
        'productos_detalles':productos_detalles,
        'foto_lista':foto_lista,
    }

    return render(request,"productos_detalles.html",context=context)
@login_required
def agregar_al_carrito(request, producto_id):
    producto=get_object_or_404(Producto,id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(cliente=request.user.cliente)
    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not item_creado:
        item.cantidad+=1
        item.save()

    messages.success(request,f'Se ha añado{producto.nombre_producto} al carrito.')

    return redirect('productos_detalles', id=producto_id)

@login_required
def ver_carrito(request):
    carrito=Carrito.objects.get(cliente=request.user.cliente)
    items=ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.costo_producto * item.cantidad for item in items)


    context = {
        'carrito':carrito,
        'items':items,
        'total':total,
    }
    
    return render(request,'ver_carrito.html',context=context)

