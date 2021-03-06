# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-29 00:23
from __future__ import unicode_literals

import db_comments.model_mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20181122_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.URLField()),
                ('size', models.BigIntegerField(default=0)),
                ('mime_type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'document',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('display_order', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=120, null=True, unique=True)),
            ],
            options={
                'db_table': 'document_category',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='DocumentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'document_history',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='DocumentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('display_order', models.IntegerField()),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=25, null=True, unique=True)),
            ],
            options={
                'db_table': 'document_status',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('the_type', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='api.DocumentCategory')),
            ],
            options={
                'db_table': 'document_type',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
        migrations.RemoveField(
            model_name='organizationattachment',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='organizationattachment',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='organizationattachment',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='effective_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='expiration_date',
        ),
        migrations.AlterField(
            model_name='organizationtype',
            name='display_order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrganizationAttachment',
        ),
        migrations.AddField(
            model_name='documenttype',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documenttype_CREATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documenttype',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documenttype_UPDATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentstatus',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documentstatus_CREATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentstatus',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documentstatus_UPDATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documenthistory_CREATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='creating_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Organization'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history_entries', to='api.Document'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='modifying_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='modifying_user_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='role', to='api.Role'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DocumentStatus'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DocumentType'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documenthistory_UPDATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentcategory',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documentcategory_CREATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentcategory',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_documentcategory_UPDATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_document_CREATE_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='creating_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Organization'),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DocumentStatus'),
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DocumentType'),
        ),
        migrations.AddField(
            model_name='document',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_document_UPDATE_USER', to=settings.AUTH_USER_MODEL),
        ),
    ]
