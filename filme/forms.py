from django import forms

from .models import Filmes, Generos

class FormFilmes(forms.ModelForm):
	class Meta:
		model = Filmes
		fields = ['filme','genero','disponivel','preco','lancamento','imagem']

class FormGeneros(forms.ModelForm):
	class Meta:
		model = Generos
		fields=['genero']
