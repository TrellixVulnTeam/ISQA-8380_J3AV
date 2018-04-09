# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('long', models.DecimalField(decimal_places=2, max_digits=50)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=50)),
                ('type', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocationVisitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='worldmap.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='locationvisitors',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='worldmap.Visitor'),
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='worldmap.Region'),
        ),
    ]