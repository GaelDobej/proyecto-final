from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.decorators import *

# Create your views here.

def encyclopedia(request):
    all = {"aEscultores": Escultor.objects.all(), 
            "aPintores": Pintor.objects.all(),
            "aEscritores": Escritor.objects.all(),
            "aIlustradores": Ilustrador.objects.all(),
            "aMusicos": Musico.objects.all(),
            "aGrabadores": Grabador.objects.all(),
            "aAnimadores": Animador.objects.all(),
            "aFotografos": Fotografo.objects.all(),
            "aCineastas": Cineasta.objects.all(),
            "aActores": Actor.objects.all(),}
    return render(request, "Salute_dEncyclopedia/home.html", all)

def back(request):
    return redirect(' ')



# -------- Artistas
def escultor(request):
    contexto = {"Escultores": Escultor.objects.all()}
    return render(request, "Salute_dEncyclopedia/aescultor.html", contexto)
@login_required
def updateEscultor(request, id_escultor):
    escultor = Escultor.objects.get(id=id_escultor)
    if request.method == "POST":
        miForm = EscultorForm(request.POST)
        if miForm.is_valid():
            escultor.nombre = miForm.cleaned_data.get("nombre")
            escultor.apellido = miForm.cleaned_data.get("apellido")
            escultor.nacimiento = miForm.cleaned_data.get("nacimiento")
            escultor.profesion = miForm.cleaned_data.get("profesion")
            escultor.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            escultor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Escultor"))
    else:
        miForm = EscultorForm(initial={
            "nombre": escultor.nombre,
            "apellido": escultor.apellido,
            "nacimiento": escultor.nacimiento,
            "profesion": escultor.profesion,
            "nacionalidad": escultor.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/aescultorUpdate.html", {"form": miForm})
@login_required
def deleteEscultor(request, id_escultor):
    escultor = Escultor.objects.get(id=id_escultor)
    escultor.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Escultor"))
@login_required
def createEscultor(request):
    if request.method == "POST":
        miForm = EscultorForm(request.POST)
        if miForm.is_valid():
            escultor_nombre = miForm.cleaned_data.get("nombre")
            escultor_apellido = miForm.cleaned_data.get("apellido")
            escultor_nacimiento = miForm.cleaned_data.get("nacimiento")
            escultor_profesion = miForm.cleaned_data.get("profesion")
            escultor_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            escultor = Escultor(nombre=escultor_nombre,
                                apellido=escultor_apellido,
                                nacimiento=escultor_nacimiento,
                                profesion=escultor_profesion,
                                nacionalidad=escultor_nacionalidad,
                                )
            escultor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Escultor"))
    else:
        miForm = EscultorForm()
    return render(request, "Salute_dEncyclopedia/aescultorUpdate.html", {"form": miForm})
#-
def pintor(request):
    contexto = {"Pintores": Pintor.objects.all()}
    return render(request, "Salute_dEncyclopedia/apintor.html", contexto)
@login_required
def updatePintor(request, id_pintor):
    pintor = Pintor.objects.get(id=id_pintor)
    if request.method == "POST":
        miForm = PintorForm(request.POST)
        if miForm.is_valid():
            pintor.nombre = miForm.cleaned_data.get("nombre")
            pintor.apellido = miForm.cleaned_data.get("apellido")
            pintor.nacimiento = miForm.cleaned_data.get("nacimiento")
            pintor.profesion = miForm.cleaned_data.get("profesion")
            pintor.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            pintor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Pintor"))
    else:
        miForm = PintorForm(initial={
            "nombre": pintor.nombre,
            "apellido": pintor.apellido,
            "nacimiento": pintor.nacimiento,
            "profesion": pintor.profesion,
            "nacionalidad": pintor.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/apintorUpdate.html", {"form": miForm})    
@login_required
def deletePintor(request, id_pintor):
    pintor = Pintor.objects.get(id=id_pintor)
    pintor.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Pintor"))
@login_required
def createPintor(request):
    if request.method == "POST":
        miForm = PintorForm(request.POST)
        if miForm.is_valid():
            pintor_nombre = miForm.cleaned_data.get("nombre")
            pintor_apellido = miForm.cleaned_data.get("apellido")
            pintor_nacimiento = miForm.cleaned_data.get("nacimiento")
            pintor_profesion = miForm.cleaned_data.get("profesion")
            pintor_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            pintor = Pintor(nombre=pintor_nombre,
                                apellido=pintor_apellido,
                                nacimiento=pintor_nacimiento,
                                profesion=pintor_profesion,
                                nacionalidad=pintor_nacionalidad,
                                )
            pintor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Pintor"))
    else:
        miForm = PintorForm()
    return render(request, "Salute_dEncyclopedia/apintorUpdate.html", {"form": miForm})
#-
def escritor(request):
    contexto = {"Escritores": Escritor.objects.all()}
    return render(request, "Salute_dEncyclopedia/aescritor.html", contexto)
@login_required
def updateEscritor(request, id_escritor):
    escritor = Escritor.objects.get(id=id_escritor)
    if request.method == "POST":
        miForm = EscritorForm(request.POST)
        if miForm.is_valid():
            escritor.nombre = miForm.cleaned_data.get("nombre")
            escritor.apellido = miForm.cleaned_data.get("apellido")
            escritor.nacimiento = miForm.cleaned_data.get("nacimiento")
            escritor.profesion = miForm.cleaned_data.get("profesion")
            escritor.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            escritor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Escritor"))
    else:
        miForm = EscritorForm(initial={
            "nombre": escritor.nombre,
            "apellido": escritor.apellido,
            "nacimiento": escritor.nacimiento,
            "profesion": escritor.profesion,
            "nacionalidad": escritor.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/aescritorUpdate.html", {"form": miForm})
@login_required
def deleteEscritor(request, id_escritor):
    escritor = Escritor.objects.get(id=id_escritor)
    escritor.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Escritor"))
@login_required
def createEscritor(request):
    if request.method == "POST":
        miForm = EscritorForm(request.POST)
        if miForm.is_valid():
            escritor_nombre = miForm.cleaned_data.get("nombre")
            escritor_apellido = miForm.cleaned_data.get("apellido")
            escritor_nacimiento = miForm.cleaned_data.get("nacimiento")
            escritor_profesion = miForm.cleaned_data.get("profesion")
            escritor_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            escritor = Escritor(nombre=escritor_nombre,
                                apellido=escritor_apellido,
                                nacimiento=escritor_nacimiento,
                                profesion=escritor_profesion,
                                nacionalidad=escritor_nacionalidad,
                                )
            escritor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Escritor"))
    else:
        miForm = EscritorForm()
    return render(request, "Salute_dEncyclopedia/aescritorUpdate.html", {"form": miForm})
#-
def ilustrador(request):
    contexto = {"Ilustradores": Ilustrador.objects.all()}
    return render(request, "Salute_dEncyclopedia/ailustrador.html", contexto)
@login_required
def updateIlustrador(request, id_ilustrador):
    ilustrador = Ilustrador.objects.get(id=id_ilustrador)
    if request.method == "POST":
        miForm = IlustradorForm(request.POST)
        if miForm.is_valid():
            ilustrador.nombre = miForm.cleaned_data.get("nombre")
            ilustrador.apellido = miForm.cleaned_data.get("apellido")
            ilustrador.nacimiento = miForm.cleaned_data.get("nacimiento")
            ilustrador.profesion = miForm.cleaned_data.get("profesion")
            ilustrador.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            ilustrador.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Ilustrador"))
    else:
        miForm = IlustradorForm(initial={
            "nombre": ilustrador.nombre,
            "apellido": ilustrador.apellido,
            "nacimiento": ilustrador.nacimiento,
            "profesion": ilustrador.profesion,
            "nacionalidad": ilustrador.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/ailustradorUpdate.html", {"form": miForm})
@login_required
def deleteIlustrador(request, id_ilustrador):
    ilustrador = Ilustrador.objects.get(id=id_ilustrador)
    ilustrador.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Ilustrador"))
@login_required
def createIlustrador(request):
    if request.method == "POST":
        miForm = IlustradorForm(request.POST)
        if miForm.is_valid():
            ilustrador_nombre = miForm.cleaned_data.get("nombre")
            ilustrador_apellido = miForm.cleaned_data.get("apellido")
            ilustrador_nacimiento = miForm.cleaned_data.get("nacimiento")
            ilustrador_profesion = miForm.cleaned_data.get("profesion")
            ilustrador_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            ilustrador = Ilustrador(nombre=ilustrador_nombre,
                                apellido=ilustrador_apellido,
                                nacimiento=ilustrador_nacimiento,
                                profesion=ilustrador_profesion,
                                nacionalidad=ilustrador_nacionalidad,
                                )
            ilustrador.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Ilustrador"))
    else:
        miForm = IlustradorForm()
    return render(request, "Salute_dEncyclopedia/ailustradorUpdate.html", {"form": miForm})
#-
def musico(request):
    contexto = {"Musicos": Musico.objects.all()}
    return render(request, "Salute_dEncyclopedia/amusico.html", contexto)
@login_required
def updateMusico(request, id_musico):
    musico = Musico.objects.get(id=id_musico)
    if request.method == "POST":
        miForm = MusicoForm(request.POST)
        if miForm.is_valid():
            musico.nombre = miForm.cleaned_data.get("nombre")
            musico.apellido = miForm.cleaned_data.get("apellido")
            musico.nacimiento = miForm.cleaned_data.get("nacimiento")
            musico.profesion = miForm.cleaned_data.get("profesion")
            musico.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            musico.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Musico"))
    else:
        miForm = MusicoForm(initial={
            "nombre": musico.nombre,
            "apellido": musico.apellido,
            "nacimiento": musico.nacimiento,
            "profesion": musico.profesion,
            "nacionalidad": musico.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/amusicoUpdate.html", {"form": miForm})
@login_required
def deleteMusico(request, id_musico):
    musico = Musico.objects.get(id=id_musico)
    musico.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Musico"))
@login_required
def createMusico(request):
    if request.method == "POST":
        miForm = MusicoForm(request.POST)
        if miForm.is_valid():
            musico_nombre = miForm.cleaned_data.get("nombre")
            musico_apellido = miForm.cleaned_data.get("apellido")
            musico_nacimiento = miForm.cleaned_data.get("nacimiento")
            musico_profesion = miForm.cleaned_data.get("profesion")
            musico_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            musico = Musico(nombre=musico_nombre,
                            apellido=musico_apellido,
                            nacimiento=musico_nacimiento,
                            profesion=musico_profesion,
                            nacionalidad=musico_nacionalidad,
                            )
            musico.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Musico"))
    else:
        miForm = MusicoForm()
    return render(request, "Salute_dEncyclopedia/amusicoUpdate.html", {"form": miForm})
#-
def grabador(request):
    contexto = {"Grabadores": Grabador.objects.all()}
    return render(request, "Salute_dEncyclopedia/agrabador.html", contexto)
@login_required
def updateGrabador(request, id_grabador):
    grabador = Grabador.objects.get(id=id_grabador)
    if request.method == "POST":
        miForm = GrabadorForm(request.POST)
        if miForm.is_valid():
            grabador.nombre = miForm.cleaned_data.get("nombre")
            grabador.apellido = miForm.cleaned_data.get("apellido")
            grabador.nacimiento = miForm.cleaned_data.get("nacimiento")
            grabador.profesion = miForm.cleaned_data.get("profesion")
            grabador.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            grabador.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Grabador"))
    else:
        miForm = GrabadorForm(initial={
            "nombre": grabador.nombre,
            "apellido": grabador.apellido,
            "nacimiento": grabador.nacimiento,
            "profesion": grabador.profesion,
            "nacionalidad": grabador.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/agrabadorUpdate.html", {"form": miForm})
@login_required
def deleteGrabador(request, id_grabador):
    grabador = Grabador.objects.get(id=id_grabador)
    grabador.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Grabador"))
@login_required
def createGrabador(request):
    if request.method == "POST":
        miForm = GrabadorForm(request.POST)
        if miForm.is_valid():
            grabador_nombre = miForm.cleaned_data.get("nombre")
            grabador_apellido = miForm.cleaned_data.get("apellido")
            grabador_nacimiento = miForm.cleaned_data.get("nacimiento")
            grabador_profesion = miForm.cleaned_data.get("profesion")
            grabador_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            grabador = Grabador(nombre=grabador_nombre,
                                apellido=grabador_apellido,
                                nacimiento=grabador_nacimiento,
                                profesion=grabador_profesion,
                                nacionalidad=grabador_nacionalidad,
                                )
            grabador.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Grabador"))
    else:
        miForm = GrabadorForm()
    return render(request, "Salute_dEncyclopedia/agrabadorUpdate.html", {"form": miForm})
#-
def animador(request):
    contexto = {"Animadores": Animador.objects.all()}
    return render(request, "Salute_dEncyclopedia/animador.html", contexto)
@login_required
def updateAnimador(request, id_animador):
    animador = Animador.objects.get(id=id_animador)
    if request.method == "POST":
        miForm = AnimadorForm(request.POST)
        if miForm.is_valid():
            animador.nombre = miForm.cleaned_data.get("nombre")
            animador.apellido = miForm.cleaned_data.get("apellido")
            animador.nacimiento = miForm.cleaned_data.get("nacimiento")
            animador.profesion = miForm.cleaned_data.get("profesion")
            animador.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            animador.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Animador"))
    else:
        miForm = AnimadorForm(initial={
            "nombre": animador.nombre,
            "apellido": animador.apellido,
            "nacimiento": animador.nacimiento,
            "profesion": animador.profesion,
            "nacionalidad": animador.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/animadorUpdate.html", {"form": miForm})
@login_required
def deleteAnimador(request, id_animador):
    animador = Animador.objects.get(id=id_animador)
    animador.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Animador"))
@login_required
def createAnimador(request):
    if request.method == "POST":
        miForm = AnimadorForm(request.POST)
        if miForm.is_valid():
            animador_nombre = miForm.cleaned_data.get("nombre")
            animador_apellido = miForm.cleaned_data.get("apellido")
            animador_nacimiento = miForm.cleaned_data.get("nacimiento")
            animador_profesion = miForm.cleaned_data.get("profesion")
            animador_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            animador = Animador(nombre=animador_nombre,
                                apellido=animador_apellido,
                                nacimiento=animador_nacimiento,
                                profesion=animador_profesion,
                                nacionalidad=animador_nacionalidad,
                                )
            animador.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Animador"))
    else:
        miForm = AnimadorForm()
    return render(request, "Salute_dEncyclopedia/animadorUpdate.html", {"form": miForm})
#-
def fotografo(request):
    contexto = {"Fotografos": Fotografo.objects.all()}
    return render(request, "Salute_dEncyclopedia/afotografo.html", contexto)
@login_required
def updateFotografo(request, id_fotografo):
    fotografo = Fotografo.objects.get(id=id_fotografo)
    if request.method == "POST":
        miForm = FotografoForm(request.POST)
        if miForm.is_valid():
            fotografo.nombre = miForm.cleaned_data.get("nombre")
            fotografo.apellido = miForm.cleaned_data.get("apellido")
            fotografo.nacimiento = miForm.cleaned_data.get("nacimiento")
            fotografo.profesion = miForm.cleaned_data.get("profesion")
            fotografo.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            fotografo.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Fotografo"))
    else:
        miForm = FotografoForm(initial={
            "nombre": fotografo.nombre,
            "apellido": fotografo.apellido,
            "nacimiento": fotografo.nacimiento,
            "profesion": fotografo.profesion,
            "nacionalidad": fotografo.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/afotografoUpdate.html", {"form": miForm})
@login_required
def deleteFotografo(request, id_fotografo):
    fotografo = Fotografo.objects.get(id=id_fotografo)
    fotografo.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Fotografo"))
@login_required
def createFotografo(request):
    if request.method == "POST":
        miForm = FotografoForm(request.POST)
        if miForm.is_valid():
            fotografo_nombre = miForm.cleaned_data.get("nombre")
            fotografo_apellido = miForm.cleaned_data.get("apellido")
            fotografo_nacimiento = miForm.cleaned_data.get("nacimiento")
            fotografo_profesion = miForm.cleaned_data.get("profesion")
            fotografo_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            fotografo = Fotografo(nombre=fotografo_nombre,
                                apellido=fotografo_apellido,
                                nacimiento=fotografo_nacimiento,
                                profesion=fotografo_profesion,
                                nacionalidad=fotografo_nacionalidad,
                                )
            fotografo.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Fotografo"))
    else:
        miForm = FotografoForm()
    return render(request, "Salute_dEncyclopedia/afotografoUpdate.html", {"form": miForm})
#-
def cineasta(request):
    contexto = {"Cineastas": Cineasta.objects.all()}
    return render(request, "Salute_dEncyclopedia/acineasta.html", contexto)
@login_required
def updateCineasta(request, id_cineasta):
    cineasta = Cineasta.objects.get(id=id_cineasta)
    if request.method == "POST":
        miForm = CineastaForm(request.POST)
        if miForm.is_valid():
            cineasta.nombre = miForm.cleaned_data.get("nombre")
            cineasta.apellido = miForm.cleaned_data.get("apellido")
            cineasta.nacimiento = miForm.cleaned_data.get("nacimiento")
            cineasta.profesion = miForm.cleaned_data.get("profesion")
            cineasta.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            cineasta.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Cineasta"))
    else:
        miForm = CineastaForm(initial={
            "nombre": cineasta.nombre,
            "apellido": cineasta.apellido,
            "nacimiento": cineasta.nacimiento,
            "profesion": cineasta.profesion,
            "nacionalidad": cineasta.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/acineastaUpdate.html", {"form": miForm})
@login_required
def deleteCineasta(request, id_cineasta):
    cineasta = Cineasta.objects.get(id=id_cineasta)
    cineasta.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Cineasta"))
@login_required
def createCineasta(request):
    if request.method == "POST":
        miForm = CineastaForm(request.POST)
        if miForm.is_valid():
            cineasta_nombre = miForm.cleaned_data.get("nombre")
            cineasta_apellido = miForm.cleaned_data.get("apellido")
            cineasta_nacimiento = miForm.cleaned_data.get("nacimiento")
            cineasta_profesion = miForm.cleaned_data.get("profesion")
            cineasta_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            cineasta = Cineasta(nombre=cineasta_nombre,
                                apellido=cineasta_apellido,
                                nacimiento=cineasta_nacimiento,
                                profesion=cineasta_profesion,
                                nacionalidad=cineasta_nacionalidad,
                                )
            cineasta.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Cineasta"))
    else:
        miForm = CineastaForm()
    return render(request, "Salute_dEncyclopedia/acineastaUpdate.html", {"form": miForm})
#-
def actor(request):
    contexto = {"Actores": Actor.objects.all()}
    return render(request, "Salute_dEncyclopedia/actor.html", contexto)
@login_required
def updateActor(request, id_actor):
    actor = Actor.objects.get(id=id_actor)
    if request.method == "POST":
        miForm = ActorForm(request.POST)
        if miForm.is_valid():
            actor.nombre = miForm.cleaned_data.get("nombre")
            actor.apellido = miForm.cleaned_data.get("apellido")
            actor.nacimiento = miForm.cleaned_data.get("nacimiento")
            actor.profesion = miForm.cleaned_data.get("profesion")
            actor.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            actor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Actor"))
    else:
        miForm = ActorForm(initial={
            "nombre": actor.nombre,
            "apellido": actor.apellido,
            "nacimiento": actor.nacimiento,
            "profesion": actor.profesion,
            "nacionalidad": actor.nacionalidad,
        })
    return render(request, "Salute_dEncyclopedia/actorUpdate.html", {"form": miForm})
@login_required
def deleteActor(request, id_actor):
    actor = Actor.objects.get(id=id_actor)
    actor.delete()
    return redirect(reverse_lazy("Salute_dEncyclopedia:Actor"))
@login_required
def createActor(request):
    if request.method == "POST":
        miForm = ActorForm(request.POST)
        if miForm.is_valid():
            actor_nombre = miForm.cleaned_data.get("nombre")
            actor_apellido = miForm.cleaned_data.get("apellido")
            actor_nacimiento = miForm.cleaned_data.get("nacimiento")
            actor_profesion = miForm.cleaned_data.get("profesion")
            actor_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            actor = Actor(nombre=actor_nombre,
                                apellido=actor_apellido,
                                nacimiento=actor_nacimiento,
                                profesion=actor_profesion,
                                nacionalidad=actor_nacionalidad,
                                )
            actor.save()
            return redirect(reverse_lazy("Salute_dEncyclopedia:Actor"))
    else:
        miForm = ActorForm()
    return render(request, "Salute_dEncyclopedia/actorUpdate.html", {"form": miForm})


