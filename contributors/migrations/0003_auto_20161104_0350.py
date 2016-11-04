# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0002_auto_20161101_1726'),
        ('contributors', '0002_auto_20161101_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='tributes',
            field=models.ManyToManyField(blank=True, to='taxes.Tax'),
        ),
        migrations.AddField(
            model_name='property',
            name='tributes',
            field=models.ManyToManyField(blank=True, to='taxes.Tax'),
        ),
    ]
