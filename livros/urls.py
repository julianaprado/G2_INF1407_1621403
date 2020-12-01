from django.urls.conf import path
from livros import views

app_name = 'livros'

urlpatterns = [
    path('cria/', views.LivroCreateView.as_view(), name='cria-Livros'),
    path('atualiza/<int:pk>/', views.LivroUpdateView.as_view(), name= 'atualiza-Livros'),
    path('apaga/<int:pk>/', views.LivroDeleteView.as_view(), name='apaga-Livros'),
    path('lista/', views.ListaLivrosView.as_view(), name='lista-Livros'),
    path('', views.ListaLivrosView.as_view(),name='home-Livros')
]
