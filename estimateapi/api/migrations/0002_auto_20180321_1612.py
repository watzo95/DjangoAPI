# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='stroski',
            field=models.CharField(max_length=200),
        ),
    ]
