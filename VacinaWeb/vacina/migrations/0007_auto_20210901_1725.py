# Generated by Django 2.2 on 2021-09-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0006_vacina_qtd_dose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='qtd_dose',
            field=models.IntegerField(default=1, verbose_name='Qtd_dose'),
        ),
    ]
