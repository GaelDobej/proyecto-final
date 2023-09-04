from django.db import models

# Create your models here.

class Escultor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')

    class Meta:
        verbose_name = "Escultor"
        verbose_name_plural = "Escultores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pintor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')
    class Meta:
        verbose_name = "Pintor"
        verbose_name_plural = "Pintores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Escritor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')
    
    class Meta:
        verbose_name = "Escritor"
        verbose_name_plural = "Escritores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Ilustrador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')
    
    class Meta:
        verbose_name = "Ilustrador"
        verbose_name_plural = "Ilustradores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Grabador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')

    class Meta:
        verbose_name = "Grabador"
        verbose_name_plural = "Grabadores"

    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Animador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')

    class Meta:
        verbose_name = "Animador"
        verbose_name_plural = "Animadores"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Fotografo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cineasta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(default="Desconocido")
    profesion = models.CharField(max_length=50, default='Sin profesión especificada')
    nacionalidad = models.CharField(max_length=50, default='Sin nacionalidad especificada')

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actores"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"