# Generated by Django 5.0.2 on 2024-02-19 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='coef_variacao',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='acao',
            name='desvio_padrao',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='acao',
            name='media',
            field=models.FloatField(),
        ),
    ]
