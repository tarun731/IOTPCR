# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-07 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govnportal', '0003_fundusagebills'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundusagebills',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
