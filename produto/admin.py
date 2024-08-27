from django.contrib import admin
from produto import models

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'preco_marketing', 'preco_marketing_promocional',
    inlines = [
        VariacaoInline
    ]

@admin.register(models.Variacao)
class VaricaoAdmin(admin.ModelAdmin):
    ...
