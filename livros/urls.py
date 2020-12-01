from django.urls.conf import path
from livros import views

app_name = 'livros'

urlpatterns = [
    path('lista/', views.ListaLivrosView.as_view(), name='lista-Livros'),
    path('', views.ListaLivrosView.as_view(),name='home-livros')
]
