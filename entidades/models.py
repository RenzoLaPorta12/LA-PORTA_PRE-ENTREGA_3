from django.db import models
from entidades.choices import *

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return "Vendedor: {}, {}".format(self.apellido, self.nombre)
    
    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ["nombre", "apellido"]

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}/ año {}".format(self.marca, self.modelo, self.año)

    class Meta:
        verbose_name = "Automovil"
        verbose_name_plural = "Automoviles"
        ordering = ["modelo", "marca", "año"]

class Usuario(models.Model):
    nombre_de_usuario = models.CharField(max_length=50, unique = True)
    email = models.EmailField(max_length=100, unique = True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return f"user: {self.nombre_de_usuario}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Reseña(models.Model):
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    contenido = models.TextField()

    def __str__(self):
        return "{} - {} estrellas".format(self.usuario, self.puntuacion)

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ["usuario", "puntuacion"]

class Compra(models.Model):
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.usuario} - {self.automovil} - {self.metodo_pago}"

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Coompras"
        ordering = ["usuario"]