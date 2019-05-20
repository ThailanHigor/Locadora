from django.db import models

class Generos(models.Model):
	genero = models.CharField('Genero',max_length = 100)
	
	class Meta:
		verbose_name = 'Genero'
		verbose_name_plural = 'Generos'
		ordering = ['genero']

	def __str__(self):
		return self.genero

class Filmes(models.Model):
	filme = models.CharField('Nome',max_length = 100)#null=True, blank=True
	genero = models.ForeignKey(Generos, on_delete=models.PROTECT) 
	disponivel = models.CharField('Disponível', max_length=10, default='Sim')
	preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
	lancamento = models.BooleanField(default=False)
	imagem = models.ImageField(upload_to = "static/imagens/",blank=True)
	ano = models.IntegerField('Ano',default=0)
	sinopse = models.TextField('sinopse', max_length=300, default='')
	trailer = models.CharField('trailer', max_length=100, blank=True)

	class Meta:
		verbose_name = 'Filme'
		verbose_name_plural = 'Filmes'
		ordering = ['filme']

	def __str__(self):
		return self.filme

class Pedido(models.Model):
	cliente= models.CharField('Nome',max_length=30)
	filme= models.ForeignKey(Filmes, on_delete=models.PROTECT)

	class Meta:
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'
		ordering = ['cliente']

	def __str__(self):
		return str(self.filme)