from django.contrib import admin

from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    # configura a forma como os dados são exibidos na area adm
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')

    # configura em quais das informações poderam ter links clicáveis
    list_display_links = ('id', 'nome', 'sobrenome')

    # insere um filtro dos dados
    list_filter = ('nome', 'sobrenome')

    # configura o número de dados mostrados por página
    list_per_page = 1

    # configura um campo de pesquisa nos campos informados
    search_fields = ('nome', 'sobrenome', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
