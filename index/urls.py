from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("luisa", views.luisa, name="luisa"),
]

"""Argumentos da função path:
Segundo argumento: a view que deve ser renderizada quando esta URL for visitada; view.nomeDaFunção,
o views representa o arquivo das views(views.py), já o nomeDaFunção é alguma função presente no arquivo views.py 
que representa uma página de visualização.

Terceiro argumento: o caminho, que representa este URL.
Veremos porquê dar um nome a um padrão de URL facilita a referência a ele em outras partes do aplicativo """

""" Essa variável urlpatterns é 
uma lista de todos os URLs permitidos 
que podem ser acessados para este aplicativo."""