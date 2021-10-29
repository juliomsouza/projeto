from django.contrib import admin
from projeto.core.models import Produtos

@admin.register(Produtos)
class ModelProdutosAdmin(admin.ModelAdmin):
    list_display = ['name', 'description'] 
