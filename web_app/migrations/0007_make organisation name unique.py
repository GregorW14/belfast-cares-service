# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-04 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_auto_20161022_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='name'),
        ),
    ]