from django.urls import path
from galeria.views import index, login

urlpatterns = [
    path('login/', login, name='login'),
    path('index/', index, name='index'),
]