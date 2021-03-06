# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-17 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0159_schedulesummary_credits_offset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledsheet',
            name='fuel_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.FuelClass'),
        ),
        migrations.AlterField(
            model_name='scheduledsheet',
            name='fuel_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.ApprovedFuel'),
        ),
    ]
