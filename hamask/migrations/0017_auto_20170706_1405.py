# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamask', '0016_workout_exercise_log_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='percentage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='reps',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='rpe',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='sets',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_exercise_log',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout_log',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
