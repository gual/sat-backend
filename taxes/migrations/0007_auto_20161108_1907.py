# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0006_auto_20161108_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declarationpaymentmode',
            name='declaration_since',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='declarationpaymentmode',
            name='declaration_until',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='declarationpaymentmode',
            name='payment_since',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='declarationpaymentmode',
            name='payment_until',
            field=models.DateField(),
        ),
    ]