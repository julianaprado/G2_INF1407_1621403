from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50, help_text='Titulo')
    dataPublicacao = models.DateField(null=True, help_text='Data de Publicação')
    autor = models.CharField(max_length=30, help_text='Nome do Autor')
    preco = models.DecimalField(max_digits=5, decimal_places=2, help_text='Preço por exemplar')
    quantidadeExemplares = models.IntegerField(help_text='Qtd de Exemplares')
    @classmethod
    def create(cls, titulo, dataPublicacao, autor, preco, quantidadeExemplares):
        livro = cls(titulo=titulo, dataPublicacao=dataPublicacao,autor=autor, preco=preco,quantidadeExemplares=quantidadeExemplares)
        return livro
