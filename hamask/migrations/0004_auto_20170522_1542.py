# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamask', '0003_auto_20170522_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifter_stats',
            name='entry_date',
            field=models.DateField(),
        ),
    ]