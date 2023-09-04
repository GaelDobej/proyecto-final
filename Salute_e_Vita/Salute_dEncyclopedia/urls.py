from django.urls import path, include
from .views import *

app_name = 'Salute_dEncyclopedia'

urlpatterns = [
    path('encyclopedia/', encyclopedia, name="Encyclopedia"),
    path('back/', back, name='back'),

# -------- Artistas
    path('escultor/', escultor, name="Escultor"),
    path('pintor/', pintor, name='Pintor'),
    path('escritor/', escritor, name="Escritor"),
    path('ilustrador/', ilustrador, name="Ilustrador"),
    path('musico/', musico, name="Musico"),
    path('grabador/', grabador, name="Grabador"),
    path('animador/', animador, name="Animador"),
    path('fotografo/', fotografo, name="Fotografo"),
    path('cineasta/', cineasta, name="Cineasta"),
    path('actor/', actor, name="Actor"),

# -------- Update
    path('update_musico/<id_musico>/', updateMusico, name='update_musico' ),
    path('update_pintor/<id_pintor>/', updatePintor, name='update_pintor' ),
    path('update_escritor/<id_escritor>/', updateEscritor, name='update_escritor' ),
    path('update_ilustrador/<id_ilustrador>/', updateIlustrador, name='update_ilustrador' ),
    path('update_escultor/<id_escultor>/', updateEscultor, name='update_escultor' ),
    path('update_fotografo/<id_fotografo>/', updateFotografo, name='update_fotografo' ),
    path('update_cineasta/<id_cineasta>/', updateCineasta, name='update_cineasta' ),
    path('update_actor/<id_actor>/', updateActor, name='update_actor' ),
    path('update_grabador/<id_grabador>/', updateGrabador, name='update_grabador' ),
    path('update_animador/<id_animador>/', updateAnimador, name='update_animador' ),

# -------- Delete
    path('delete_musico/<id_musico>/', deleteMusico, name='delete_musico' ),
    path('delete_pintor/<id_pintor>/', deletePintor, name='delete_pintor' ),
    path('delete_escritor/<id_escritor>/', deleteEscritor, name='delete_escritor' ),
    path('delete_ilustrador/<id_ilustrador>/', deleteIlustrador, name='delete_ilustrador' ),
    path('delete_escultor/<id_escultor>/', deleteEscultor, name='delete_escultor' ),
    path('delete_fotografo/<id_fotografo>/', deleteFotografo, name='delete_fotografo' ),
    path('delete_cineasta/<id_cineasta>/', deleteCineasta, name='delete_cineasta' ),
    path('delete_actor/<id_actor>/', deleteActor, name='delete_actor' ),
    path('delete_grabador/<id_grabador>/', deleteGrabador, name='delete_grabador' ),
    path('delete_animador/<id_animador>/', deleteAnimador, name='delete_animador' ),

# -------- Create
    path('create_musico/', createMusico, name='create_musico' ),
    path('create_pintor/', createPintor, name='create_pintor' ),
    path('create_escritor/', createEscritor, name='create_escritor' ),
    path('create_ilustrador/', createIlustrador, name='create_ilustrador' ),
    path('create_escultor/', createEscultor, name='create_escultor' ),
    path('create_fotografo/', createFotografo, name='create_fotografo' ),
    path('create_cineasta/', createCineasta, name='create_cineasta' ),
    path('create_actor/', createActor, name='create_actor' ),
    path('create_grabador/', createGrabador, name='create_grabador' ),
    path('create_animador/', createAnimador, name='create_animador' ),
]

