from django.db import models
from django.contrib.auth.models import User

"""
Professor, eu não consegui fazer com que o foreignKey do funcionário fosse automatico, eu cheguei a por editable=False, para ele sumir
mas para isso o default=User desse certe e não deu. Portanto, para um livro aparecer, é preciso que o campo esteja editavel para que voce
possa atribuir o username ao livro.
"""


class Livro(models.Model):
    Funcionario = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    titulo = models.CharField(max_length=50, help_text='Titulo')
    dataPublicacao = models.DateField(null=True, help_text='Data de Publicação')
    autor = models.CharField(max_length=30, help_text='Nome do Autor')
    preco = models.DecimalField(max_digits=5, decimal_places=2, help_text='Preço por exemplar')
    quantidadeExemplares = models.IntegerField(help_text='Qtd de Exemplares')
    
    
    @classmethod
    def create(cls, titulo, dataPublicacao, autor, preco, quantidadeExemplares):
        livro = cls(titulo=titulo, dataPublicacao=dataPublicacao,autor=autor, preco=preco,quantidadeExemplares=quantidadeExemplares)
        return livro

    
    def __str__(self):
        return self.field_name
