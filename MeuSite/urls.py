"""MeuSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    re_path(r'^(?P<path>.*)/$', views.ListaLivrosView.as_view()),
    path('',views.ListaLivrosView.as_view()),

"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),

    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/',views.registro,name='sec-registro'),

    path('accounts/login/', LoginView.as_view(template_name='registro/login.html'), name='sec-login'),
    path('accounts/profile/', views.paginaSecreta, name='sec-paginaSecreta'),

    path('accounts/password-change/',PasswordChangeView.as_view(template_name='registro/password_change_form.html', success_url=reverse_lazy('sec-password_change_done')), name='sec-password_change'),
    path('accounts/password-change-done/',PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html'), name='sec-password_change_done'),
]
