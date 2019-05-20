from django.conf.urls import url
from django.contrib import admin
from filme.views import filmes_list,\
generos_list,index,filmes_search,generos_search,busca_filme,not_found,do_login,\
 do_logout,perfil,add_pedido,confirmar_compra

urlpatterns = [
	url(r'^$',index,name='index'), #lançamentos
	url(r'^generos_list/$',generos_list, name='generos_list'),
	url(r'^generos_search/(?P<generos>[0-9]+)/$',generos_search,name='generos_search'),

	
	url(r'^filmes_list/$',filmes_list, name='filmes_list'),
	url(r'^filmes_search/(?P<letra>[a-zA-Z]+)/$',filmes_search, name='filmes_search'),
	url(r'^busca_filme/$',busca_filme, name='busca_filme'),


	url(r'^login/$',do_login, name='do_login'),
	url(r'^logout/$',do_logout, name='do_logout'),

	url(r'^perfil/$',perfil, name='perfil'),
	url(r'^add_pedido/(?P<pk>[0-9]+)/$',add_pedido, name='add_pedido'),
	url(r'^confirmar_compra/(?P<pk>[0-9]+)/$',confirmar_compra, name='confirmar_compra'),

	url(r'^not_found/$',not_found, name='not_found'),
	url(r'^admin/', admin.site.urls)
]