from django.contrib import admin
from .models import Member, Livre, DVD, CD, JeuDePlateau, Emprunt

admin.site.register(Member)
admin.site.register(Livre)
admin.site.register(DVD)
admin.site.register(CD)
admin.site.register(JeuDePlateau)
admin.site.register(Emprunt)