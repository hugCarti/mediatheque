from django.db import models
from django.utils import timezone


class Media(models.Model):
    name = models.CharField(max_length=255)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Membre', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class Livre(Media):
    auteur = models.CharField(max_length=255)


class DVD(Media):
    realisateur = models.CharField(max_length=255)


class CD(Media):
    artiste = models.CharField(max_length=255)


class JeuDePlateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)


class Membre(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)
