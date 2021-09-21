from django.contrib import admin
from .models import Vacina


@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'qtd_dose', 'lote' )