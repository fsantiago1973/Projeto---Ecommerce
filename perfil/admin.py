from django.contrib import admin
from perfil import models

class EnderecoInline(admin.TabularInline):
    model = models.Endereco
    extra = 1

@admin.register(models.Perfil)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        EnderecoInline
    ]

@admin.register(models.Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    ...
