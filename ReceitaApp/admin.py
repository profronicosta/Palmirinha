from django.contrib import admin
from ReceitaApp.models import Receita, Categoria
from django.utils.html import mark_safe

class ReceitaAdmin(admin.ModelAdmin):
    readonly_fields = ['ver_imagem']

    def ver_imagem(self, obj):
        return mark_safe(f'<img src="{obj.imagem.url}" width="75" height="75" />')

# Register your models here.
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Categoria)
