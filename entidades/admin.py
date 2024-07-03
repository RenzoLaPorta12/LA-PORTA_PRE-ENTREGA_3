from django.contrib import admin
# Register your models here.
from entidades.models import *

admin.site.register(Usuario)
admin.site.register(Vendedor)
admin.site.register(Automovil)
admin.site.register(Reseña)
admin.site.register(Compra)