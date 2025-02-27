from django.test import TestCase
from .models import Member, Livre, Emprunt

class MemberTestCase(TestCase):
    def test_creation_membre(self):
        member = Member.objects.create(name="Jean Dupont")
        self.assertEqual(member.name, "Jean Dupont")

class LoanTestCase(TestCase):
    def test_emprunt(self):
        member = Member.objects.create(name="Jean Dupont")
        livre = Livre.objects.create(name="Le Petit Prince", auteur="Antoine de Saint-Exupéry")
        emprunt = Emprunt.objects.create(media=livre, member=member)
        self.assertEqual(emprunt.member.name, "Jean Dupont")
        self.assertEqual(emprunt.media.name, "Le Petit Prince")