# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-21 16:52
from __future__ import unicode_literals

import db_comments.model_mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_document_link_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('fuel_code', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('carbon_intensity', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=999, null=True)),
                ('application_date', models.DateField(blank=True, null=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('fuel', models.CharField(blank=True, max_length=100, null=True)),
                ('feedstock', models.CharField(blank=True, max_length=100, null=True)),
                ('feedstock_location', models.CharField(blank=True, max_length=100, null=True)),
                ('feedstock_misc', models.CharField(blank=True, max_length=100, null=True)),
                ('facility_location', models.CharField(blank=True, max_length=100, null=True)),
                ('facility_nameplate', models.IntegerField(blank=True, null=True)),
                ('feedstock_transport_mode', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel_transport_mode', models.CharField(blank=True, max_length=100, null=True)),
                ('former_company', models.CharField(blank=True, max_length=100, null=True)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelcode_CREATE_USER', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelcode_UPDATE_USER', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fuel_code',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
    ]
