from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(EnderecoEntrega)