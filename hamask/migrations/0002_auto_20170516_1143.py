# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='lifter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hamask.Lifter'),
        ),
    ]
