from django.contrib import admin
from livros.models import Livro
admin.site.register(Livro)

class LivroInstanceAdmin(admin.ModelAdmin):
    lista_display= ('Funcionario','titulo','dataPublicacao','autor')
    
    fieldsets = (
        (None, {
            'fields': ('titulo','preco', 'quantidadeExemplares')
        }),
        ('Availability', {
            'fields': ('ehFuncionario')
        }),
    )