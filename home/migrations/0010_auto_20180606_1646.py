# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-06 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_faviconimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faviconimage',
            options={'verbose_name': 'Фавікон', 'verbose_name_plural': 'Фавікони'},
        ),
        migrations.AddField(
            model_name='faviconimage',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]