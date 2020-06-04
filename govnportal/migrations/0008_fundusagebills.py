# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-04-08 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('govnportal', '0007_auto_20200408_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundusagebills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('bill', models.ImageField(upload_to='')),
                ('date', models.DateField(null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='govnportal.Branches')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='govnportal.Funds')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='govnportal.Organization')),
            ],
        ),
    ]