from django.contrib import admin

from core.models import Carro, Categoria, Cor, Marca

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Cor)
admin.site.register(Carro)

# Register your models here.
