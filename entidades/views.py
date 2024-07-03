from django.shortcuts import render
from entidades.models import *

from entidades.forms import * 
# Create your views here.

def home(request):
    return render(request, "entidades/index.html")
def usuario(request):
    contexto = {"Usuario": Usuario.objects.all()}
    return render(request, "entidades/usuario.html", contexto)
def eresVendedor(request):
    contexto = {"Vendedor": Vendedor.objects.all()}
    return render(request, "entidades/eresVendedor.html", contexto)
def reseña(request):
    contexto = {"Reseña": Reseña.objects.all()}
    return render(request, "entidades/reseña.html", contexto)
def vender(request):
    contexto = {"Automovil": Automovil.objects.all()}
    return render(request, "entidades/vender.html", contexto)
def comprar(request):
    contexto = {"Compra": Compra.objects.all()}
    return render(request, "entidades/comprar.html", contexto)



#añadidos

def about(request):
    return render(request, "entidades/about.html")
def terminos(request):
    return render(request, "entidades/terminos.html")
def privacidad(request):
    return render(request, "entidades/privacidad.html")
def contact(request):
    return render(request, "entidades/contact.html")

#Formuularios:

def vendedorForm(request):
    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        if miForm.is_valid():
            vendor_nombre = miForm.cleaned_data.get("nombre")
            vendor_apellido = miForm.cleaned_data.get("apellido")
            vendedor_email = miForm.cleaned_data.get("email")
            vendedor_telefono = miForm.cleaned_data.get("telefono")
            vendedor_direccion = miForm.cleaned_data.get("direccion")
            vendedor = Vendedor(nombre=vendor_nombre, apellido=vendor_apellido, email=vendedor_email, telefono=vendedor_telefono, direccion=vendedor_direccion)
            vendedor.save()
            contexto = {"Vendedor": Vendedor.objects.all()}
            return render(request, "entidades/eresVendedor.html", contexto)

    else:
        miForm = VendedorForm()

    return render(request, "entidades/vendedorForm.html", {"form": miForm})


def automovilForm(request):
    if request.method == "POST":
        miForm = AutomovilForm(request.POST)
        if miForm.is_valid():
            automovil_marca = miForm.cleaned_data.get("marca")
            automovil_modelo = miForm.cleaned_data.get("modelo")
            automovil_año = miForm.cleaned_data.get("año")
            automovil_precio = miForm.cleaned_data.get("precio")
            automovil_descripcion = miForm.cleaned_data.get("descripcion")
            automovil_vendedor = miForm.cleaned_data.get("vendedor")
            automovil = Automovil(marca=automovil_marca, modelo=automovil_modelo,año=automovil_año,precio=automovil_precio,descripcion=automovil_descripcion,vendedor=automovil_vendedor)
            automovil.save()
            contexto = {"Automovil": Automovil.objects.all()}
            return render(request, "entidades/vender.html", contexto)

    else:
        miForm = AutomovilForm()

    return render(request, "entidades/automovilForm.html", {"form": miForm})


def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get("nombre_de_usuario")
            usuario_email = miForm.cleaned_data.get("email")
            usuario_contraseña = miForm.cleaned_data.get("contraseña")
            usuario = Usuario(nombre_de_usuario=usuario_nombre, email=usuario_email, contraseña=usuario_contraseña)
            usuario.save()
            contexto = {"Usuario": Usuario.objects.all()}
            return render(request, "entidades/usuario.html", contexto)
    else:
        miForm = UsuarioForm()

    return render(request, "entidades/usuarioForm.html", {"form": miForm})

def reseñaForm(request):
    if request.method == "POST":
        miForm = ReseñaForm(request.POST)
        if miForm.is_valid():
            reseña_automovil= miForm.cleaned_data.get("automovil")
            reseña_usuario = miForm.cleaned_data.get("usuario")
            reseña_puntuacion = miForm.cleaned_data.get("puntuacion")
            reseña_contenido = miForm.cleaned_data.get("contenido")
            reseña = Reseña(automovil=reseña_automovil, usuario=reseña_usuario, puntuacion=reseña_puntuacion, contenido=reseña_contenido)
            reseña.save()
            contexto = {"Reseña": Reseña.objects.all()}
            return render(request, "entidades/reseña.html", contexto)
    else:
        miForm = ReseñaForm()

    return render(request, "entidades/reseñaForm.html", {"form": miForm})

def compraForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            compra_automovil= miForm.cleaned_data.get("automovil")
            compra_usuario = miForm.cleaned_data.get("usuario")
            compra_metodo_pago = miForm.cleaned_data.get("contenido")
            compra = Compra(automovil=compra_automovil, usuario=compra_usuario, metodo_pago=compra_metodo_pago)
            reseña.save()
            contexto = {"Compra": Compra.objects.all()}
            return render(request, "entidades/compra.html", contexto)
    else:
        miForm = CompraForm()

    return render(request, "entidades/compraForm.html", {"form": miForm})

#buscar 

def buscarAutomovil(request):
    return render (request, "entidades/buscarAutomovil.html")

def encontrarAutomovil(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        autos = Automovil.objects.filter(marca__icontains=patron)
        contexto = {'automovil': autos}
    else:
        contexto = {'automovil': Automovil.objects.all()}
    return render(request, "entidades/vender.html", contexto)