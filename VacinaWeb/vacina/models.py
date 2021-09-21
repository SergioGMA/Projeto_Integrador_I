from django.db import models

class Vacina(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, default="Name")
    desc = models.CharField(verbose_name='Desc', max_length=100, default="Desc")
    qtd_dose = models.IntegerField(verbose_name='Qtd_dose', default=1)
    lote = models.CharField(verbose_name='lote', max_length=100, default="lote")
