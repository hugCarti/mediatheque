from django.urls import path
from .views import liste_medias, creer_membre, liste_membres

urlpatterns = [
    path('medias/', liste_medias, name='liste_medias'),
    path('membres/', liste_membres, name='liste_membres'),
    path('membres/creer/', creer_membre, name='creer_membre'),
]
