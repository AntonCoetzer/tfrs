# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0088_auto_20190228_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelcodestatus',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelcodestatus',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
