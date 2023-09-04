from django.shortcuts import redirect, render
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth       import *
from django.contrib.auth.decorators import *
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "Salute_cHome/base.html")


# -------- Login / Logout / Register

def loginRequest(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            password = miForm.cleaned_data.get("password")
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
 
                return redirect("home")
            else:
                return render(request, "Salute_cHome/login.html", {"form": miForm, "mensaje":"Los datos son invalidos."})

        else:
            return render(request, "Salute_cHome/login.html", {"form": miForm, "mensaje":"Los datos son invalidos."})
        
    miForm = AuthenticationForm()
    return render(request, "Salute_cHome/login.html", {"form": miForm,})


def register(request):
    if request.method == "POST":
        miForm = RegistroUsuario(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect("home")
    else:
        miForm = RegistroUsuario()
    return render(request, "Salute_cHome/registro.html", {"form": miForm})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get("email")
            usuario.password1 = form.cleaned_data.get("password1")
            usuario.password2 = form.cleaned_data.get("password2")
            usuario.profesion = form.cleaned_data.get("profesion")
            usuario.first_name = form.cleaned_data.get("first_name")
            usuario.last_name = form.cleaned_data.get("last_name")
            usuario.save()
            return redirect("home")
        else:
            return render(request, "Salute_cHome/editarPerfil.html", {"form": form, "usuario": usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "Salute_cHome/editarPerfil.html", {"form": form, "usuario": usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return redirect("home")
    else:
        form = AvatarFormulario()
    return render(request, "Salute_cHome/agregarAvatar.html", {"form": form})

