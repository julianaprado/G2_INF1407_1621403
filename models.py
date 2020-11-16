from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    data_publicacao = models.DateField(null=True)
    autor = models.CharField(max_length=30, blank=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_exemplares = models.IntegerField()
