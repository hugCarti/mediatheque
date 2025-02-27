from django import forms
from .models import Member, Media, Emprunt

class CreatMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']

class CreatLoanForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['media', 'member']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer les médias disponibles et les members non bloqués
        self.fields['media'].queryset = Media.objects.filter(disponible=True)
        self.fields['member'].queryset = Member.objects.filter(bloque=False)