from django.contrib import admin
from .models import Conferencia, Conferencista, Participante, Asistencia

class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora',)
    list_editable = ('nombre',) #las tuplas con solo un elemento debe llevar una coma para que entienda que es una tupla

admin.site.register(Conferencia, ConferenciaAdmin)

admin.site.register(Conferencista)

admin.site.register(Participante)

admin.site.register(Asistencia)
