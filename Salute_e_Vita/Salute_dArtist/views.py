from django.shortcuts import redirect, render
from .models import *
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.contrib.auth.mixins import *
from django.contrib.auth.models import *
from django.contrib.auth.decorators import *
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

def back(request):
    return redirect('/#artistas')


#____with Class Based View

class EscritorList(LoginRequiredMixin, ListView):
    model = Escritor

class EscritorCreate(LoginRequiredMixin, CreateView):
    model = Escritor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Escritor")

class EscritorUpdate(LoginRequiredMixin, UpdateView):
    model = Escritor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Escritor")    

class EscritorDelete(LoginRequiredMixin, DeleteView):
    model = Escritor
    success_url = reverse_lazy("Salute_dArtist:Escritor")
#____

class PintorList(LoginRequiredMixin, ListView):
    model = Pintor

class PintorCreate(LoginRequiredMixin, CreateView):
    model = Pintor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Pintor")

class PintorUpdate(LoginRequiredMixin, UpdateView):
    model = Pintor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Pintor")    

class PintorDelete(LoginRequiredMixin, DeleteView):
    model = Pintor
    success_url = reverse_lazy("Salute_dArtist:Pintor")

#____
class EscultorList(LoginRequiredMixin, ListView):
    model = Escultor

class EscultorCreate(LoginRequiredMixin, CreateView):
    model = Escultor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Escultor")

class EscultorUpdate(LoginRequiredMixin, UpdateView):
    model = Escultor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Escultor")    

class EscultorDelete(LoginRequiredMixin, DeleteView):
    model = Escultor
    success_url = reverse_lazy("Salute_dArtist:Escultor")
#____

class IlustradorList(LoginRequiredMixin, ListView):
    model = Ilustrador

class IlustradorCreate(LoginRequiredMixin, CreateView):
    model = Ilustrador
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Ilustrador")

class IlustradorUpdate(LoginRequiredMixin, UpdateView):
    model = Ilustrador
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Ilustrador")    

class IlustradorDelete(LoginRequiredMixin, DeleteView):
    model = Ilustrador
    success_url = reverse_lazy("Salute_dArtist:Ilustrador")
#____
class MusicoList(LoginRequiredMixin, ListView):
    model = Musico

class MusicoCreate(LoginRequiredMixin, CreateView):
    model = Musico
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Musico")

class MusicoUpdate(LoginRequiredMixin, UpdateView):
    model = Musico
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Musico")    

class MusicoDelete(LoginRequiredMixin, DeleteView):
    model = Musico
    success_url = reverse_lazy("Salute_dArtist:Musico")
#____
class GrabadorList(LoginRequiredMixin, ListView):
    model = Grabador

class GrabadorCreate(LoginRequiredMixin, CreateView):
    model = Grabador
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Grabador")

class GrabadorUpdate(LoginRequiredMixin, UpdateView):
    model = Grabador
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Grabador")    

class GrabadorDelete(LoginRequiredMixin, DeleteView):
    model = Grabador
    success_url = reverse_lazy("Salute_dArtist:Grabador")
#____

class AnimadorList(LoginRequiredMixin, ListView):
    model = Animador

class AnimadorCreate(LoginRequiredMixin, CreateView):
    model = Animador
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Animador")

class AnimadorUpdate(LoginRequiredMixin, UpdateView):
    model = Animador
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Animador")    

class AnimadorDelete(LoginRequiredMixin, DeleteView):
    model = Animador
    success_url = reverse_lazy("Salute_dArtist:Animador")
#____

class FotografoList(LoginRequiredMixin, ListView):
    model = Fotografo

class FotografoCreate(LoginRequiredMixin, CreateView):
    model = Fotografo
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Fotografo")

class FotografoUpdate(LoginRequiredMixin, UpdateView):
    model = Fotografo
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Animador")    

class FotografoDelete(LoginRequiredMixin, DeleteView):
    model = Fotografo
    success_url = reverse_lazy("Salute_dArtist:Fotografo")
#____

class CineastaList(LoginRequiredMixin, ListView):
    model = Cineasta

class CineastaCreate(LoginRequiredMixin, CreateView):
    model = Cineasta
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Cineasta")

class CineastaUpdate(LoginRequiredMixin, UpdateView):
    model = Cineasta
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Cineasta")    

class CineastaDelete(LoginRequiredMixin, DeleteView):
    model = Cineasta
    success_url = reverse_lazy("Salute_dArtist:Cineasta")
#____

class ActorList(LoginRequiredMixin, ListView):
    model = Actor

class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Actor")

class ActorUpdate(LoginRequiredMixin, UpdateView):
    model = Actor
    fields = ["nombre", "apellido", "nacionalidad", "portfolio"]
    success_url = reverse_lazy("Salute_dArtist:Actor")    

class ActorDelete(LoginRequiredMixin, DeleteView):
    model = Actor
    success_url = reverse_lazy("Salute_dArtist:Actor")
#____




#____Servicios

def musiservice(request):
    contexto = {"ServiciosMu": ServicioMusicalModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosMusico.html", contexto)

def musico_agregar_Servicio(request):
    if request.method == "POST":
        miForm = MusicoServiceForm(request.POST)
        if miForm.is_valid():
            musicoservice_titulo = miForm.cleaned_data.get("titulo")
            musicoservice_descripcion = miForm.cleaned_data.get("descripcion")
            musicoservice_contacto = miForm.cleaned_data.get("contacto")
            musicoservice = ServicioMusicalModel(
                                    titulo=musicoservice_titulo,
                                    descripcion=musicoservice_descripcion,
                                    contacto=musicoservice_contacto,
                                    )
            musicoservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_musical"))
    else:
        miForm = MusicoServiceForm()
    return render(request, "Salute_dArtist/musico_agre_servicio.html", {"form": miForm})
#_
def pintoservice(request):
    contexto = {"ServiciosPi": ServicioPintorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosPintor.html", contexto)

def pintor_agregar_Servicio(request):
    if request.method == "POST":
        miForm = PintorServiceForm(request.POST)
        if miForm.is_valid():
            pintorservice_titulo = miForm.cleaned_data.get("titulo")
            pintorservice_descripcion = miForm.cleaned_data.get("descripcion")
            pintorservice_contacto = miForm.cleaned_data.get("contacto")
            pintorservice = ServicioPintorModel(
                                    titulo=pintorservice_titulo,
                                    descripcion=pintorservice_descripcion,
                                    contacto=pintorservice_contacto,
                                    )
            pintorservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_pintor"))
    else:
        miForm = PintorServiceForm()
    return render(request, "Salute_dArtist/pintor_agre_servicio.html", {"form": miForm})
#_
def ilustrservice(request):
    contexto = {"ServiciosIl": ServicioIlustradorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosIlustrador.html", contexto)

def ilustrador_agregar_Servicio(request):
    if request.method == "POST":
        miForm = IlustradorServiceForm(request.POST)
        if miForm.is_valid():
            ilustradorservice_titulo = miForm.cleaned_data.get("titulo")
            ilustradorservice_descripcion = miForm.cleaned_data.get("descripcion")
            ilustradorservice_contacto = miForm.cleaned_data.get("contacto")
            ilustradorservice = ServicioIlustradorModel(
                                    titulo=ilustradorservice_titulo,
                                    descripcion=ilustradorservice_descripcion,
                                    contacto=ilustradorservice_contacto,
                                    )
            ilustradorservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_ilustrador"))
    else:
        miForm = IlustradorServiceForm()
    return render(request, "Salute_dArtist/pintor_agre_servicio.html", {"form": miForm})
#_
def grabaservice(request):
    contexto = {"ServiciosGr": ServicioGrabadorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosGrabador.html", contexto)

def grabador_agregar_Servicio(request):
    if request.method == "POST":
        miForm = GrabadorServiceForm(request.POST)
        if miForm.is_valid():
            grabadorservice_titulo = miForm.cleaned_data.get("titulo")
            grabadorservice_descripcion = miForm.cleaned_data.get("descripcion")
            grabadorservice_contacto = miForm.cleaned_data.get("contacto")
            grabadorservice = ServicioGrabadorModel(
                                    titulo=grabadorservice_titulo,
                                    descripcion=grabadorservice_descripcion,
                                    contacto=grabadorservice_contacto,
                                    )
            grabadorservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_grabador"))
    else:
        miForm = GrabadorServiceForm()
    return render(request, "Salute_dArtist/grabador_agre_servicio.html", {"form": miForm})
#_
def fotograservice(request):
    contexto = {"ServiciosFo": ServicioFotografoModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosFotografo.html", contexto)

def fotografo_agregar_Servicio(request):
    if request.method == "POST":
        miForm = FotografoServiceForm(request.POST)
        if miForm.is_valid():
            fotografoservice_titulo = miForm.cleaned_data.get("titulo")
            fotografoservice_descripcion = miForm.cleaned_data.get("descripcion")
            fotografoservice_contacto = miForm.cleaned_data.get("contacto")
            fotografoservice = ServicioFotografoModel(
                                    titulo=fotografoservice_titulo,
                                    descripcion=fotografoservice_descripcion,
                                    contacto=fotografoservice_contacto,
                                    )
            fotografoservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_fotografo"))
    else:
        miForm = FotografoServiceForm()
    return render(request, "Salute_dArtist/fotografo_agre_servicio.html", {"form": miForm})
#_
def esculservice(request):
    contexto = {"ServiciosEs": ServicioEscultorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosEscultor.html", contexto)

def escultor_agregar_Servicio(request):
    if request.method == "POST":
        miForm = EscultorServiceForm(request.POST)
        if miForm.is_valid():
            escultrservice_titulo = miForm.cleaned_data.get("titulo")
            escultrservice_descripcion = miForm.cleaned_data.get("descripcion")
            escultrservice_contacto = miForm.cleaned_data.get("contacto")
            escultrservice = ServicioEscultorModel(
                                    titulo=escultrservice_titulo,
                                    descripcion=escultrservice_descripcion,
                                    contacto=escultrservice_contacto,
                                    )
            escultrservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_escultor"))
    else:
        miForm = EscultorServiceForm()
    return render(request, "Salute_dArtist/escultor_agre_servicio.html", {"form": miForm})
#_
def escriservice(request):
    contexto = {"ServiciosEsc": ServicioEscritorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosEscritor.html", contexto)

def escritor_agregar_Servicio(request):
    if request.method == "POST":
        miForm = EscritorServiceForm(request.POST)
        if miForm.is_valid():
            escritorservice_titulo = miForm.cleaned_data.get("titulo")
            escritorservice_descripcion = miForm.cleaned_data.get("descripcion")
            escritorservice_contacto = miForm.cleaned_data.get("contacto")
            escritorservice = ServicioEscritorModel(
                                    titulo=escritorservice_titulo,
                                    descripcion=escritorservice_descripcion,
                                    contacto=escritorservice_contacto,
                                    )
            escritorservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_escritor"))
    else:
        miForm = EscritorServiceForm()
    return render(request, "Salute_dArtist/escritor_agre_servicio.html", {"form": miForm})
#_
def cineaservice(request):
    contexto = {"ServiciosCi": ServicioCineastaModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosCineasta.html", contexto)

def cineasta_agregar_Servicio(request):
    if request.method == "POST":
        miForm = CineastaServiceForm(request.POST)
        if miForm.is_valid():
            cineastaservice_titulo = miForm.cleaned_data.get("titulo")
            cineastaservice_descripcion = miForm.cleaned_data.get("descripcion")
            cineastaservice_contacto = miForm.cleaned_data.get("contacto")
            cineastaservice = ServicioCineastaModel(
                                    titulo=cineastaservice_titulo,
                                    descripcion=cineastaservice_descripcion,
                                    contacto=cineastaservice_contacto,
                                    )
            cineastaservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_cineasta"))
    else:
        miForm = CineastaServiceForm()
    return render(request, "Salute_dArtist/cineasta_agre_servicio.html", {"form": miForm})
#_
def animaservice(request):
    contexto = {"ServiciosAn": ServicioAnimadorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosAnimador.html", contexto)

def animador_agregar_Servicio(request):
    if request.method == "POST":
        miForm = AnimadorServiceForm(request.POST)
        if miForm.is_valid():
            animadorservice_titulo = miForm.cleaned_data.get("titulo")
            animadorservice_descripcion = miForm.cleaned_data.get("descripcion")
            animadorservice_contacto = miForm.cleaned_data.get("contacto")
            animadorservice = ServicioAnimadorModel(
                                    titulo=animadorservice_titulo,
                                    descripcion=animadorservice_descripcion,
                                    contacto=animadorservice_contacto,
                                    )
            animadorservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_animador"))
    else:
        miForm = AnimadorServiceForm()
    return render(request, "Salute_dArtist/animador_agre_servicio.html", {"form": miForm})
#_
def actoservice(request):
    contexto = {"ServiciosAc": ServicioActorModel.objects.all()}
    return render(request, "Salute_dArtist/serviciosActor.html", contexto)

def actor_agregar_Servicio(request):
    if request.method == "POST":
        miForm = ActorServiceForm(request.POST)
        if miForm.is_valid():
            actorservice_titulo = miForm.cleaned_data.get("titulo")
            actorservice_descripcion = miForm.cleaned_data.get("descripcion")
            actorservice_contacto = miForm.cleaned_data.get("contacto")
            actorservice = ServicioActorModel(
                                    titulo=actorservice_titulo,
                                    descripcion=actorservice_descripcion,
                                    contacto=actorservice_contacto,
                                    )
            actorservice.save()
            return redirect(reverse_lazy("Salute_dArtist:servicio_actor"))
    else:
        miForm = ActorServiceForm()
    return render(request, "Salute_dArtist/actor_agre_servicio.html", {"form": miForm})
