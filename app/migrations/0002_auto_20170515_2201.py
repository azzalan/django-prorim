# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='disponibilidade',
            field=models.CharField(max_length=150, verbose_name='Disponibilidade'),
        ),
    ]