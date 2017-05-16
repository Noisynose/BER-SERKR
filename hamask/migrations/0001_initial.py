# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 15:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('has_stats', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lifter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('measurement_system', models.CharField(choices=[('IMPER', 'Imperial'), ('METRC', 'Metric')], default='METRC', max_length=30)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('sex', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEML', 'Female')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lifter_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default=datetime.date.today)),
                ('reps', models.PositiveIntegerField(blank=True)),
                ('weight', models.PositiveIntegerField(blank=True)),
                ('time', models.PositiveIntegerField(blank=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hamask.Exercise')),
                ('lifter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Lifter')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('start_date', models.DateField(blank=True)),
                ('is_current', models.BooleanField(default=False)),
                ('auto_update_stats', models.BooleanField(default=True)),
                ('rounding', models.CharField(choices=[('NO', 'No rounding'), ('2.5', '2.5'), ('5', '5'), ('10', '10'), ('LAST_5', 'Last digit is 5')], default='NO', max_length=30)),
                ('lifter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Lifter')),
            ],
        ),
        migrations.CreateModel(
            name='Rep_Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField(blank=True)),
                ('reps', models.PositiveIntegerField(blank=True)),
                ('weight', models.PositiveIntegerField(blank=True)),
                ('percentage', models.PositiveIntegerField(blank=True)),
                ('rpe', models.PositiveIntegerField(blank=True)),
                ('time', models.PositiveIntegerField(blank=True)),
                ('is_amrap', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hamask.Exercise')),
                ('rep_scheme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hamask.Rep_Scheme')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Workout')),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Exercise_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField(blank=True)),
                ('reps', models.PositiveIntegerField(blank=True)),
                ('weight', models.PositiveIntegerField(blank=True)),
                ('percentage', models.PositiveIntegerField(blank=True)),
                ('rpe', models.PositiveIntegerField(blank=True)),
                ('time', models.PositiveIntegerField(blank=True)),
                ('is_amrap', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('Workout_Exercise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hamask.Workout_Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('workout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hamask.Workout')),
            ],
        ),
        migrations.AddField(
            model_name='workout_exercise_log',
            name='Workout_Log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Workout_Log'),
        ),
        migrations.AddField(
            model_name='workout',
            name='workout_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Workout_Group'),
        ),
        migrations.AddField(
            model_name='program',
            name='rep_scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hamask.Rep_Scheme'),
        ),
        migrations.AddField(
            model_name='lifter_stats',
            name='workout_exercise_log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hamask.Workout_Exercise_Log'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='lifter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamask.Lifter'),
        ),
    ]
