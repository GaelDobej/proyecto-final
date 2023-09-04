from django.db import models

# Create your models here.

class Escultor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Escultor"
        verbose_name_plural = "Escultores"

    def __str__(self):
        return f"{self.nombre}"

class Pintor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Pintor"
        verbose_name_plural = "Pintores"

    def __str__(self):
        return f"{self.nombre}"

class Escritor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Escritor"
        verbose_name_plural = "Escritores"

    def __str__(self):
        return f"{self.nombre}"

class Ilustrador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Ilustrador"
        verbose_name_plural = "Ilustradores"

    def __str__(self):
        return f"{self.nombre}"

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Musico"
        verbose_name_plural = "Musicos"

    def __str__(self):
        return f"{self.nombre}"

class Grabador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Grabador"
        verbose_name_plural = "Grabadores"

    def __str__(self):
        return f"{self.nombre}"
    
class Animador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Animador"
        verbose_name_plural = "Animadores"

    def __str__(self):
        return f"{self.nombre}"

class Fotografo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Fotografo"
        verbose_name_plural = "Fotografos"

    def __str__(self):
        return f"{self.nombre}"

class Cineasta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Cineasta"
        verbose_name_plural = "Cineastas"

    def __str__(self):
        return f"{self.nombre}"

class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    portfolio = models.URLField(default = " ")
    nacionalidad = models.CharField(max_length=50, default=' ')

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actores"

    def __str__(self):
        return f"{self.nombre}"


#_________Servicios:

class ServicioMusicalModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioPintorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioIlustradorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioGrabadorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioFotografoModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioEscultorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioEscritorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioCineastaModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioAnimadorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()

class ServicioActorModel(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    contacto = models.URLField()


