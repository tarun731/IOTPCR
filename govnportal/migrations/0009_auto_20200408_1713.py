# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-04-08 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('govnportal', '0008_fundusagebills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundusagebills',
            name='fund',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='govnportal.Funds'),
        ),
    ]
