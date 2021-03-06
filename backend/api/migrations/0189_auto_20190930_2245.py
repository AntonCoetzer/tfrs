# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-30 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0188_update_roles_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='compliancereporttype',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='compliancereporttype',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_compliancereporttype_CREATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='compliancereporttype',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compliancereporttype',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compliancereporttype',
            name='update_timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='compliancereporttype',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_compliancereporttype_UPDATE_USER', to=settings.AUTH_USER_MODEL),
        ),
    ]
