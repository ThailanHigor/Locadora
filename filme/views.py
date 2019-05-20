from django.shortcuts import render, redirect
from .models import Filmes, Generos, Pedido
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
	dados = Filmes.objects.filter(lancamento=True) #Busca por lancamento
	return render(request,'index.html',{'dados':dados})

def filmes_search(request,letra):
	if letra != 'T': # T referencia para todos os filmes
		dados = Filmes.objects.filter(filme__istartswith=letra)
		if dados.count() == 0: #vazio
			return render(request,'not_found.html')
	else:
		dados = Filmes.objects.all()
	return render(request,'filmes_list.html',{'dados':dados})


def filmes_list(request):
	dados = Filmes.objects.all()
	return render(request,'filmes_list.html',{'dados':dados})

def busca_filme(request):
	if request.method == 'POST':
		campo = request.POST.get('buscafilme') #obtem o filme buscado
		dados = Filmes.objects.filter(filme__icontains=campo) #case insentive buscando o filme
		if dados.count() == 0: #vazio
			return render(request,'not_found.html')
		else:
			return render(request,'filmes_list.html',{'dados':dados})

	else:
		return render(request,'filmes_list.html',{})

def not_found(request):
	return render(request,'not_found.html')


def generos_list(request):
	gen= Generos.objects.all()
	filmes = Filmes.objects.all()
	#passo as 2 listas, generos para o comboBox e filmes para listagem
	return render(request,'generos_list.html',{'filmes':filmes,'dados':gen}) 	

def generos_search(request,generos):
	gen = Generos.objects.all()
	dados = Filmes.objects.filter(genero=generos) # filtro a partir do id do genero selecionado
	if dados.count() == 0:#vazio
		return render(request,'not_found.html')
	else:
		return render(request,'generos_list.html',{'filmes':dados,'dados':gen})

@login_required
def perfil(request):
	lista= Pedido.objects.filter(cliente=str(request.user)) #lista de pedidos por usuario logado
	return render(request,'perfil.html',{'lista':lista})


@login_required
def add_pedido(request,pk):
	dados = Filmes.objects.get(pk=pk) # busca pelo ID do filme
	pedido = Pedido.objects.create(cliente=str(request.user),filme=dados) #passa instancia do filme
	pedido.save()
	return redirect('/perfil/')

@login_required
def confirmar_compra(request,pk):
	dados=Pedido.objects.get(pk=pk)
	dados.delete()
	return redirect('/perfil/')

def do_login(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		nova=request.POST.get('nova') # VERIFICA SE É NOVO USUARIO a partir do click no bota
		if nova == 'novo': # se o botao possui o valor novo que adquiriu ao ser clicado
			User.objects.create_user(username=username,email=username+'@cliente.com',password=password)
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/filmes_list/')
				
	return render(request,'login.html')

def do_logout(request):
	logout(request)
	return redirect('/filmes_list/')
