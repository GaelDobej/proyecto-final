from django.urls import path, include
from .views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('', home, name=' '),
    path("home", home, name="home"),
    path('Salute_dArtist/', include('Salute_dArtist.urls', namespace='Salute_dArtist')),
    path('encyclopedia/', include('Salute_dEncyclopedia.urls', namespace='Salute_dEncyclopedia')),



    path('login/', loginRequest, name='Login'),
    path('logout/', LogoutView.as_view(template_name="Salute_cHome/logout.html"), name='Logout'),
    path('registro/', register, name='Registro'),
    path('editar_perfil/', editarPerfil, name='editar_perfil'),
    path('agregar_avatar/', agregarAvatar, name='agregar_avatar'),
]
