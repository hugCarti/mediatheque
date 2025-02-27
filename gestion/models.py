from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Livre(Media):
    auteur = models.CharField(max_length=100)

class DVD(Media):
    realisateur = models.CharField(max_length=100)

class CD(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

class Emprunt(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.name} - {self.media.name}"