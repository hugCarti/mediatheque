from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil (menu principal)
    path('', views.menu_bibliotheque, name='menu_bibliotheque'),

    # URLs pour les médias
    path('medias/', views.list_medias, name='list_medias'),

    # URLs pour les membres
    path('membres/', views.list_member, name='list_member'),
    path('membres/creer/', views.creat_member, name='creat_member'),

    # URLs pour les emprunts
    path('emprunts/creer/', views.creat_loan, name='creat_loan'),
    path('emprunts/retour/<int:emprunt_id>/', views.loan_return, name='loan_return'),
]