from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from livros.models import Livro
from livros.forms import LivrosModelToForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

class ListaLivrosView(View):
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

class LivroCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario': LivrosModelToForm,}
        return render(request, "livros/criaLivro.html",context)

    def post(self, request, *arg, **kwargs):
        formulario = LivrosModelToForm(request.POST)
        if formulario.is_valid():
            livro = formulario.save()
            livro.save()
            return HttpResponseRedirect(reverse_lazy("livros:lista-Livros"))

class LivroUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        livro = Livro.objects.get(pk=pk)
        formulario=LivrosModelToForm(instance=livro)
        context = {'livro':formulario, }
        return render(request, 'livros/atualizaLivro.html', context)

    def post(slef, request, pk, *args, **kwargs):
        livro = get_object_or_404(Livro, pk=pk)
        formulario = LivrosModelToForm(instance=pessoa)
        if formulario.is_valid():
            livro = formulario.save()
            pessoa.save()
            return HttpResponseRedirect(reverse_lazy("livroos:lista-Livros"))
        else:
            context = {'livro': formulario,}
            return render(request, 'livros/atualizaLivro.html', context)

class LivroDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        livro = Livro.objects.get(pk=pk)
        context = {'livro': livro,}
        return render(request, 'livros/apagaLivro.html', context)

    def post(self, request, pk, *args, **kwargs):
        livro = Livro.objects.get(pk=pk)
        livro.delete()
        print("Removendo livro", pk)
        return HttpResponseRedirect(reverse_lazy("livros:lista-Livros"))
