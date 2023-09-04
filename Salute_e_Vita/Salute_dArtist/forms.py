from django import forms



class MusicoForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)


class PintorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class EscritorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class IlustradorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)   
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class CineastaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)  
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class ActorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)   
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class AnimadorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class GrabadorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class FotografoForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)   
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)

class EscultorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)  
    portfolio = forms.URLField(required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=False)


#___________Servicios:

class MusicoServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class PintorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class IlustradorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class GrabadorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class FotografoServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class EscultorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class EscritorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class CineastaServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class AnimadorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)

class ActorServiceForm(forms.Form):
    titulo = forms.CharField(label = "Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label = "Descripcion", max_length=1000, required=True)
    contacto = forms.URLField(required=True)