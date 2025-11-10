from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_boutique, name='inicio_boutique'),
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categoria/ver/', views.ver_categorias, name='ver_categorias'),
    path('categoria/actualizar/<int:categoria_id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/actualizar/realizar/<int:categoria_id>/', views.realizar_actualizacion_categoria, name='realizar_actualizacion_categoria'),
    path('categoria/borrar/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),

    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_productos, name='ver_productos'),
    path('producto/actualizar/<int:idproducto>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/borrar/<int:idproducto>/', views.borrar_producto, name='borrar_producto'),
]
