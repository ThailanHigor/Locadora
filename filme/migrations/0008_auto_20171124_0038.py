# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0007_auto_20171123_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=30, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['cliente'],
            },
        ),
        migrations.AlterField(
            model_name='filmes',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filme.Generos'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filme.Filmes'),
        ),
    ]
