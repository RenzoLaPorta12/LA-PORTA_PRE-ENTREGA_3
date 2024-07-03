from django import forms
from .models import *
from entidades.choices import *

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    telefono = forms.CharField(max_length=15, required=True)
    direccion = forms.CharField(max_length=100, required=True)

class AutomovilForm(forms.Form):
    marca = forms.CharField(max_length=100, required=True)
    modelo = forms.CharField(max_length=100, required=True)
    año = forms.IntegerField(required=True)
    precio = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(widget=forms.Textarea, required=True)
    vendedor =  forms.ModelChoiceField(queryset= Vendedor.objects.all(), required=True)

class UsuarioForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)
    contraseña = forms.CharField(max_length=100, required=True)

class ReseñaForm(forms.Form):
    automovil = forms.ModelChoiceField(queryset= Automovil.objects.all(), required=True)
    usuario = forms.ModelChoiceField(queryset= Usuario.objects.all(), required=True)
    contenido = forms.CharField(widget=forms.Textarea, required=True)

class CompraForm(forms.Form):
    automovil = forms.ModelChoiceField(queryset= Automovil.objects.all(), required=True)
    usuario = forms.ModelChoiceField(queryset= Usuario.objects.all(), required=True)
    metodo_pago = forms.CharField(max_length=50, required=True)