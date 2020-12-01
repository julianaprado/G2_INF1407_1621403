from django.shortcuts import render
from django.views.generic.base import View
from livros.models import Livro

class ListaLivros(View):

    def get(self, request, *args, **kwargs):

        # buscar todos os livros do banco de dados
        livros = Livro.objects.all()

        # dicionario de variaveis para o template
        context = {
            'livros' : livros
        }

        """
        o template vai estar dentro do diretorio lista
        o template vai se chamar listaLivros.html
        """
        return render(request, 'livros/listaLivros.html', context)
