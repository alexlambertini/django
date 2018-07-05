from django.urls import path
from .views import *


urlpatterns = [
    path('listagem', lista_clientes),
    path('', teste)
]
