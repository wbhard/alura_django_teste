from django.urls import path
from galeria.views import index, login, produto

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro-cliente/', index, name='cadastroCliente'),
    path('cadastro-produto/', produto, name='produto'),
]