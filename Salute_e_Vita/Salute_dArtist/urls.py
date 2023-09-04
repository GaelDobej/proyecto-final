from django.urls import path, include
from .views import *
from django.views.generic import ListView

app_name = 'Salute_dArtist'

urlpatterns = [

    path('back/', back, name='back'),

    path('escultor/', EscultorList.as_view(), name="Escultor"),
    path('create_escultor/', EscultorCreate.as_view(), name="create_escultor"),
    path('update_escultor/<int:pk>/', EscultorUpdate.as_view(), name="update_escultor"),
    path('delete_escultor/<int:pk>/', EscultorDelete.as_view(), name="delete_escultor"),

    path('pintor/', PintorList.as_view(), name='Pintor'),
    path('create_pintor/', PintorCreate.as_view(), name="create_pintor"),
    path('update_pintor/<int:pk>/', PintorUpdate.as_view(), name="update_pintor"),
    path('delete_pintor/<int:pk>/', PintorDelete.as_view(), name="delete_pintor"),

    path('escritor/', EscritorList.as_view(), name="Escritor"),
    path('create_escritor/', EscritorCreate.as_view(), name="create_escritor"),
    path('update_escritor/<int:pk>/', EscritorUpdate.as_view(), name="update_escritor"),
    path('delete_escritor/<int:pk>/', EscritorDelete.as_view(), name="delete_escritor"),

    path('ilustrador/', IlustradorList.as_view(), name="Ilustrador"),
    path('create_ilustrador/', IlustradorCreate.as_view(), name="create_ilustrador"),
    path('update_ilustrador/<int:pk>/', IlustradorUpdate.as_view(), name="update_ilustrador"),
    path('delete_ilustrador/<int:pk>/', IlustradorDelete.as_view(), name="delete_ilustrador"),

    path('musico/', MusicoList.as_view(), name="Musico"),
    path('create_musico/', MusicoCreate.as_view(), name="create_musico"),
    path('update_musico/<int:pk>/', MusicoUpdate.as_view(), name="update_musico"),
    path('delete_musico/<int:pk>/', MusicoDelete.as_view(), name="delete_musico"),

    path('grabador/', GrabadorList.as_view(), name="Grabador"),
    path('create_grabador/', GrabadorCreate.as_view(), name="create_grabador"),
    path('update_grabador/<int:pk>/', GrabadorUpdate.as_view(), name="update_grabador"),
    path('delete_grabador/<int:pk>/', GrabadorDelete.as_view(), name="delete_grabador"),

    path('animador/', AnimadorList.as_view(), name="Animador"),
    path('create_animador/', AnimadorCreate.as_view(), name="create_animador"),
    path('update_animador/<int:pk>/', AnimadorUpdate.as_view(), name="update_animador"),
    path('delete_animador/<int:pk>/', AnimadorDelete.as_view(), name="delete_animador"),

    path('fotografo/', FotografoList.as_view(), name="Fotografo"),
    path('create_fotografo/', FotografoCreate.as_view(), name="create_fotografo"),
    path('update_fotografo/<int:pk>/', FotografoUpdate.as_view(), name="update_fotografo"),
    path('delete_fotografo/<int:pk>/', FotografoDelete.as_view(), name="delete_fotografo"),

    path('cineasta/', CineastaList.as_view(), name="Cineasta"),
    path('create_cineasta/', CineastaCreate.as_view(), name="create_cineasta"),
    path('update_cineasta/<int:pk>/', CineastaUpdate.as_view(), name="update_cineasta"),
    path('delete_cineasta/<int:pk>/', CineastaDelete.as_view(), name="delete_cineasta"),

    path('actor/', ActorList.as_view(), name="Actor"),
    path('create_actor/', ActorCreate.as_view(), name="create_actor"),
    path('update_actor/<int:pk>/', ActorUpdate.as_view(), name="update_actor"),
    path('delete_actor/<int:pk>/', ActorDelete.as_view(), name="delete_actor"),


#_____Servicios
    path('servicio_musical/', musiservice, name="servicio_musical"),
    path('musico_agregar_servicio/', musico_agregar_Servicio, name="musico_agregar_servicio"),

    path('servicio_pintor/', pintoservice, name="servicio_pintor"),
    path('pintor_agregar_servicio/', pintor_agregar_Servicio, name="pintor_agregar_servicio"),

    path('servicio_ilustrador/', ilustrservice, name="servicio_ilustrador"),
    path('ilustrador_agregar_servicio/', ilustrador_agregar_Servicio, name="ilustrador_agregar_servicio"),

    path('servicio_grabador/', grabaservice, name="servicio_grabador"),
    path('grabador_agregar_servicio/', grabador_agregar_Servicio, name="grabador_agregar_servicio"),

    path('servicio_fotografo/', fotograservice, name="servicio_fotografo"),
    path('fotografo_agregar_servicio/', fotografo_agregar_Servicio, name="fotografo_agregar_servicio"),

    path('servicio_escultor/', esculservice, name="servicio_escultor"),
    path('escultor_agregar_servicio/', escultor_agregar_Servicio, name="escultor_agregar_servicio"),

    path('servicio_escritor/', escriservice, name="servicio_escritor"),
    path('escritor_agregar_servicio/', escritor_agregar_Servicio, name="escritor_agregar_servicio"),

    path('servicio_cineasta/', cineaservice, name="servicio_cineasta"),
    path('cineasta_agregar_servicio/', cineasta_agregar_Servicio, name="cineasta_agregar_servicio"),

    path('servicio_animador/', animaservice, name="servicio_animador"),
    path('animador_agregar_servicio/', animador_agregar_Servicio, name="animador_agregar_servicio"),

    path('servicio_actor/', actoservice, name="servicio_actor"),
    path('actor_agregar_servicio/', actor_agregar_Servicio, name="actor_agregar_servicio"),

]