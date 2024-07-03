from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('usuario/', usuario, name="usuario"),
    path('eresVendedor/', eresVendedor, name="eresVendedor"),
    path('reseña/', reseña, name="reseña"),
    path('vender/', vender, name="vender"),
    path('comprar/', comprar, name="comprar"),


    path('about/', about , name="about"),
    path('terminos_de_uso/', terminos , name="terminos"),
    path('politicas_de_privacidad/', privacidad , name="privacidad"),
    path('contact/', contact , name="contact"),

    #formularios
    path('usuario_form/', usuarioForm, name="usuarioForm"),
    path('vendedor_form/', vendedorForm, name="vendedorForm"),
    path('automovil_form/', automovilForm, name="automovilForm"),
    path('reseña_form/', reseñaForm, name="reseñaForm"),
    path('compra_form/', compraForm, name="compraForm"),

    path('buscarAutomovil/', buscarAutomovil, name="buscarAutomovil"),
    path('encontrarAutomovil/', encontrarAutomovil, name="encontrarAutomovil"),

]
