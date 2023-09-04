from django import forms

 
class ArtistForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento",required=True)  
    PROFESIONES = (
        ("Cineasta", "Cineasta"),
        ("Actor", "Actor"),
        ("Escritor", "Escritor"),
        ("Escultor", "Escultor"),
        ("Fotografo", "Fotógrafo"),
        ("Grabador", "Grabador"),
        ("Musico", "Músico"),
        ("Animador", "Animador"),
        ("Pintor", "Pintor"),
        ("Ilustrador", "Ilustrador"), )
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class MusicoForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")  
    PROFESIONES = (
        ("Musico", "Músico"), )
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class PintorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")  
    PROFESIONES = (
        ("Pintor", "Pintor"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class EscritorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")    
    PROFESIONES = (
        ("Escritor", "Escritor"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class IlustradorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")   
    PROFESIONES = (
        ("Ilustrador", "Ilustrador"), )
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class CineastaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")   
    PROFESIONES = (
        ("Cineasta", "Cineasta"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class ActorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")    
    PROFESIONES = (
        ("Actor", "Actor"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class AnimadorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")   
    PROFESIONES = (
        ("Animador", "Animador"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class GrabadorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")    
    PROFESIONES = (
        ("Grabador", "Grabador"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class FotografoForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")    
    PROFESIONES = (
        ("Fotografo", "Fotografo"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)

class EscultorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    apellido = forms.CharField(label = "Apellido",max_length=50, required=True)
    nacimiento = forms.DateField(label = "Nacimiento")   
    PROFESIONES = (
        ("Escultor", "Escultor"),)
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES, required=True)
    nacionalidad = forms.CharField(label = "Nacionalidad",max_length=50, required=True)