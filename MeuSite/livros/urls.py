from django.urls.conf import path
from livros import views

urlpatterns = [
    path('livros/', views.listaLivros.as_view(), name='listaLivros'),
]
"oi"