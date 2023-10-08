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
]



