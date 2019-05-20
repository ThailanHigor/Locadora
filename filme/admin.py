from django.contrib import admin

from .models import Filmes,Generos,Pedido

admin.site.register(Filmes,list_display = ['filme','genero','disponivel','preco','lancamento','trailer'],
	search_fields = ['filme','genero'],
	list_filter = ['filme','genero']
)
admin.site.register(Generos)

admin.site.register(Pedido)