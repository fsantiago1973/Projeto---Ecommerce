from django.contrib import admin
from pedido import models

@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    ...

@admin.register(models.ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    ...
