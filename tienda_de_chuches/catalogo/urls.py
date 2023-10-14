from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('profile_cliente/',views.profile_cliente,name='profile_cliente'),
    path('edit_profile_cliente/',views.edit_profile_cliente,name='edit_profile_cliente'),
    path('profile_empleado/',views.profile_empleado,name='profile_empleado'),
    path('new_producto/',views.new_producto,name='new_producto'),
    path('subir_foto_p/<int:pk>',views.subir_foto_p,name='subir_foto_p'),
    path('productos/',views.productos,name='productos'),
    path('productos_detalles/<int:id>',views.productos_detalles,name='productos_detalles'),
    path('catalogo/agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/',views.ver_carrito,name='ver_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/',views.eliminar_del_carrito,name='eliminar_del_carrito'),
    path('facturacion/',views.facturacion,name='facturacion'),
    path('buscar_productos_por_nombre/',views.buscar_productos_por_nombre,name='buscar_productos_por_nombre'),
]



