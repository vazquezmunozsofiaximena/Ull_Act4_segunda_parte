from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria , Producto

def inicio_boutique(request):
    total_categorias = Categoria.objects.count()
    total_productos = Producto.objects.count()

    categorias = Categoria.objects.all().order_by('-fechacreacion')[:5]
    productos = Producto.objects.all().order_by('-fechaagregado')[:4]

    return render(request, 'inicio.html', {
        'total_categorias': total_categorias,
        'total_productos': total_productos,
        'categorias': categorias,
        'productos': productos,
    })

# Agregar categoría
def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        tipo = request.POST.get('tipo')
        slug = request.POST.get('slug')
        activo = True if request.POST.get('activo') == 'on' else False

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            tipo=tipo,
            slug=slug,
            activo=activo
        )
        return redirect('ver_categorias')
    return render(request, 'categoria/agregar_categoria.html')

# Ver todas
def ver_categorias(request):
    categorias = Categoria.objects.all().order_by('nombre')
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

# Actualizar
def actualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, 'categoria/actualizar_categoria.html', {'categoria': categoria})

def realizar_actualizacion_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.tipo = request.POST.get('tipo')
        categoria.slug = request.POST.get('slug')
        categoria.activo = True if request.POST.get('activo') == 'on' else False
        categoria.save()
        return redirect('ver_categorias')
    return redirect('ver_categorias')

# Borrar
def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categoria/borrar_categoria.html', {'categoria': categoria})


# AGREGAR PRODUCTO
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('idcategoria2')  # toma el valor del select

        if categoria_id:  # 🔹 Asegurarse de que no venga vacío
            categoria = get_object_or_404(Categoria, id=categoria_id)
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                idcategoria2=categoria
            )
            return redirect('ver_productos')
        else:
            return render(request, 'producto/agregar_producto.html', {
                'categorias': Categoria.objects.all(),
                'error': 'Por favor selecciona una categoría.'
            })

    categorias = Categoria.objects.all()
    return render(request, 'producto/agregar_producto.html', {'categorias': categorias})

# VER PRODUCTOS
def ver_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'producto/ver_productos.html', {'productos': productos})

# ACTUALIZAR PRODUCTO
def actualizar_producto(request, idproducto):
    producto = get_object_or_404(Producto, id=idproducto)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')

        # ✅ Obtener la categoría seleccionada
        idcategoria2 = request.POST.get('idcategoria2')
        if idcategoria2:
            producto.idcategoria2_id = int(idcategoria2)

        producto.save()
        return redirect('ver_productos')

    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'categorias': categorias
    })

# BORRAR PRODUCTO
def borrar_producto(request, idproducto):
    producto = get_object_or_404(Producto, id=idproducto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})