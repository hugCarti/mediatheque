from django.test import TestCase
from .models import Livre, Membre

class TestModels(TestCase):
    def test_creation_livre(self):
        livre = Livre.objects.create(name="1984", auteur="George Orwell", disponible=True)
        self.assertEqual(livre.name, "1984")
        self.assertTrue(livre.disponible)

    def test_creation_membre(self):
        membre = Membre.objects.create(name="Jean Dupont")
        self.assertEqual(membre.name, "Jean Dupont")
        self.assertFalse(membre.bloque)
