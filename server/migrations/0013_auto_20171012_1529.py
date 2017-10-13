# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_auto_20170928_1737'),
    ]

    """
    Since we're just renaming the tables to lowercase, Django isn't smart enough
    to figure out that they're different. So we rename them with a _ suffix 
    before the actual rename
    """
    operations = [
        migrations.AlterModelTable(
            name='audit',
            table='audit_',
        ),
        migrations.AlterModelTable(
            name='audit',
            table='audit',
        ),
        migrations.AlterModelTable(
            name='credittrade',
            table='credit_trade_',
        ),
        migrations.AlterModelTable(
            name='credittrade',
            table='credit_trade',
        ),
        migrations.AlterModelTable(
            name='credittradehistory',
            table='credit_trade_history_',
        ),
        migrations.AlterModelTable(
            name='credittradehistory',
            table='credit_trade_history',
        ),
        migrations.AlterModelTable(
            name='credittradestatus',
            table='credit_trade_status_',
        ),
        migrations.AlterModelTable(
            name='credittradestatus',
            table='credit_trade_status',
        ),
        migrations.AlterModelTable(
            name='credittradetype',
            table='credit_trade_type_',
        ),
        migrations.AlterModelTable(
            name='credittradetype',
            table='credit_trade_type',
        ),
        migrations.AlterModelTable(
            name='fuelsupplier',
            table='fuel_supplier_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplier',
            table='fuel_supplier',
        ),
        migrations.AlterModelTable(
            name='fuelsupplieractionstype',
            table='fuel_supplier_actions_type_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplieractionstype',
            table='fuel_supplier_actions_type',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierattachment',
            table='fuel_supplier_attachment_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierattachment',
            table='fuel_supplier_attachment',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierattachmenttag',
            table='fuel_supplier_attachment_tag_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierattachmenttag',
            table='fuel_supplier_attachment_tag',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierbalance',
            table='fuel_supplier_balance_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierbalance',
            table='fuel_supplier_balance',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierccdata',
            table='fuel_supplier_c_c_data_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierccdata',
            table='fuel_supplier_c_c_data',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliercontact',
            table='fuel_supplier_contact_',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliercontact',
            table='fuel_supplier_contact',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliercontactrole',
            table='fuel_supplier_contact_role_',
        ),
        migrations.AlterModelTable(
            name='fuelsuppliercontactrole',
            table='fuel_supplier_contact_role',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierhistory',
            table='fuel_supplier_history_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierhistory',
            table='fuel_supplier_history',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierstatus',
            table='fuel_supplier_status_',
        ),
        migrations.AlterModelTable(
            name='fuelsupplierstatus',
            table='fuel_supplier_status',
        ),
        migrations.AlterModelTable(
            name='notification',
            table='notification_',
        ),
        migrations.AlterModelTable(
            name='notification',
            table='notification',
        ),
        migrations.AlterModelTable(
            name='notificationevent',
            table='notification_event_',
        ),
        migrations.AlterModelTable(
            name='notificationevent',
            table='notification_event',
        ),
        migrations.AlterModelTable(
            name='notificationtype',
            table='notification_type_',
        ),
        migrations.AlterModelTable(
            name='notificationtype',
            table='notification_type',
        ),
        migrations.AlterModelTable(
            name='permission',
            table='permission_',
        ),
        migrations.AlterModelTable(
            name='permission',
            table='permission',
        ),
    ]
