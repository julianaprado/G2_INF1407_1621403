from django.urls.conf import path
from livros import views

app_name = 'livros'

urlpatterns = [
    path('lista/', views.ListaLivros.as_view(), name='lista-Livros'),
]
