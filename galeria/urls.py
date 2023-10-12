from django.urls import path
from galeria.views import index, login, produto, home

urlpatterns = [
    path('', login, name='login'),
    path('cadastro-cliente/', index, name='cadastro-cliente'),
    path('cadastro-produto/', produto, name='cadastro-produto'),
    path('Home/', home, name='home')
]