from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from .forms import *

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __Str__(self):
        return f"{self.user}, {self.imagen}"