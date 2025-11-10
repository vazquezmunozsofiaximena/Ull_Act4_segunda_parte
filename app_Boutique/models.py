from django.db import models

# ==========================================
# MODELO: CATEGORIA
# ==========================================
class Categoria(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    fechacreacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fechaagregado = models.DateField(auto_now_add=True)
    idcategoria2 = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre


# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto',
        related_name='proveedores'
    )

    def __str__(self):
        return self.nombre