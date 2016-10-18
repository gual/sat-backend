# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import taxes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeclarationPaymentMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration_periodicity', enumfields.fields.EnumIntegerField(enum=taxes.models.Periodicity)),
                ('declaration_since', models.IntegerField()),
                ('declaration_until', models.IntegerField()),
                ('payment_periodicity', enumfields.fields.EnumIntegerField(enum=taxes.models.Periodicity)),
                ('payment_since', models.IntegerField()),
                ('payment_until', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Determinant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('condition', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_until', models.DateField(null=True)),
                ('formula', models.CharField(max_length=2000)),
                ('determinants', models.ManyToManyField(to='taxes.Determinant')),
            ],
        ),
        migrations.CreateModel(
            name='RateRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('upper_limit', models.DecimalField(decimal_places=2, max_digits=11)),
                ('lower_limit', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fixed_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('variable_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.Rate')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('origin_law', models.CharField(max_length=2000)),
                ('taxable_subject', enumfields.fields.EnumField(enum=taxes.models.TaxableSubject, max_length=10)),
                ('declaration_payment_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.DeclarationPaymentMode')),
                ('determinants', models.ManyToManyField(to='taxes.Determinant')),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.Rate')),
            ],
        ),
        migrations.CreateModel(
            name='TaxableIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('formula', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='taxableincome',
            name='tokens',
            field=models.ManyToManyField(to='taxes.Token'),
        ),
        migrations.AddField(
            model_name='tax',
            name='taxable_income',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.TaxableIncome'),
        ),
        migrations.AddField(
            model_name='rate',
            name='tokens',
            field=models.ManyToManyField(to='taxes.Token'),
        ),
    ]
