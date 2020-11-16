from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluir minhas novas urls
    # se o endereco (URL) for do tipo www.meusite.com.br/livros/---
    path('livros/', include('livros.urls'))
]
