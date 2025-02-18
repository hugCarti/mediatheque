from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre, DVD, CD, JeuDePlateau, Membre

def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'gestion/list_medias.html', {
        'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux
    })

def creer_membre(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Membre.objects.create(name=name)
        return redirect('liste_membres')
    return render(request, 'gestion/creer_membre.html')

def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'gestion/liste_membres.html', {'membres': membres})
