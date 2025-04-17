from django.contrib import admin

# Register your models here.
from .models import conteudo, Categoria

@admin.register(conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'categoria','data_lancamento','disponivel')
    list_filter = ('tipo','categoria')
    search_fields = ('titulo', 'categoria', 'tipo',)

admin.site.register(Categoria)

