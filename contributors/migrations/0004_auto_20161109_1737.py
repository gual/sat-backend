# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0003_auto_20161104_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='nit',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='social_reason',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='dui',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='nit',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='other_names',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='other_surnames',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]