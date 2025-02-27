from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre, DVD, CD, JeuDePlateau, Member, Media, Emprunt
from .forms import CreatMemberForm, CreatLoanForm

def menu_bibliotheque(request):
    return render(request, 'base.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Livre, DVD, CD, JeuDePlateau, Emprunt

def list_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'gestion/list_medias.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})

def list_member(request):
    members = Member.objects.all()
    return render(request, 'gestion/list_member.html', {'members': members})

def creat_member(request):
    if request.method == 'POST':
        form = CreatMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_members')
    else:
        form = CreatMemberForm()
    return render(request, 'gestion/creat_member.html', {'form': form})

def creat_loan(request):
    if request.method == 'POST':
        form = CreatLoanForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.media.disponible = False
            emprunt.media.save()
            emprunt.save()
            return redirect('list_medias')
    else:
        form = CreatLoanForm()
    return render(request, 'gestion/creat_loan.html', {'form': form})

def loan_return(request, loan_id):
    loan = get_object_or_404(Emprunt, id=loan_id)
    loan.media.disponible = True
    loan.media.save()
    loan.delete()
    return redirect('list_medias')