# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-29 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metailnook', '0004_auto_20180728_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='collectiondate',
            field=models.DateField(verbose_name='collectiondate'),
        ),
    ]
