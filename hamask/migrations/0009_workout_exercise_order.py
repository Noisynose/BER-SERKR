# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamask', '0008_auto_20170601_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout_exercise',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]