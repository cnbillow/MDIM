# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-09 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gypsumProducts', '0002_auto_20180809_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gypsumproduct',
            old_name='description',
            new_name='domentions',
        ),
    ]
