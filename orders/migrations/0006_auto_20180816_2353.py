# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-16 20:53
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productinbasket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=64, null=True, verbose_name='Телефон'),
        ),
    ]
