from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

"""
Professor, eu não consegui fazer com que o foreignKey do funcionário fosse automatico, eu cheguei a por editable=False, para ele sumir
mas para isso o default=User desse certe e não deu. Portanto, para um livro aparecer, é preciso que o campo esteja editavel para que voce
possa atribuir o username ao livro.
"""


class Livro(models.Model):
    Funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, help_text='Titulo', validators=[MaxLengthValidator(500, message='Nome grande demais.')])
    dataPublicacao = models.DateField(null=True, help_text='MM/DD/AAAA')
    autor = models.CharField(max_length=100, help_text='Nome do Autor', validators=[MaxLengthValidator(500, message='Nome grande demais.')])
    preco = models.DecimalField(max_digits=5, decimal_places=2, help_text='Preço por exemplar', validators=[MinValueValidator(0, message='Preço deve ser maior que zero.')])
    quantidadeExemplares = models.IntegerField(help_text='Qtd de Exemplares', verbose_name='Numero de Exemplares',validators=[MinValueValidator(0, message='Quantidade deve ser maior que zero.')])
    
    
    @classmethod
    def create(cls, titulo, dataPublicacao, autor, preco, quantidadeExemplares):
        livro = cls(titulo=titulo, dataPublicacao=dataPublicacao,autor=autor, preco=preco,quantidadeExemplares=quantidadeExemplares)
        return livro

    
    def __str__(self):
        return self.field_name
