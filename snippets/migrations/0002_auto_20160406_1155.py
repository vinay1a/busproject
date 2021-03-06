# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='code',
            new_name='BusRoute',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='title',
        ),
        migrations.AddField(
            model_name='snippet',
            name='BusNo',
            field=models.CharField(blank=True, default='KA', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='latitude',
            field=models.CharField(blank=True, default='32', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='longitude',
            field=models.CharField(blank=True, default='24', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='time',
            field=models.CharField(blank=True, default='12.20', max_length=100),
        ),
    ]
