# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0149_auto_20190612_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'compliance_report_schedule_b',
            },
        ),
        migrations.CreateModel(
            name='ScheduleBRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fuel_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.FuelClass')),
                ('fuel_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.FuelCode')),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ApprovedFuel')),
            ],
            options={
                'db_table': 'compliance_report_schedule_b_record',
            },
        ),
        migrations.AlterField(
            model_name='provisionoftheact',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='provisionoftheact',
            name='provision',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='schedulebrecord',
            name='provision_of_the_act',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ProvisionOfTheAct'),
        ),
        migrations.AddField(
            model_name='schedulebrecord',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='records', to='api.ScheduleB'),
        ),
        migrations.AddField(
            model_name='compliancereport',
            name='schedule_b',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compliance_report', to='api.ScheduleB'),
        ),
    ]
