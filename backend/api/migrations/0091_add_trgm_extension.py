from django.db import migrations, connection
from django.db.migrations import RunPython


def add_trgrm_extension(apps, schema_editor):
    """
    Add the postgresql trigram matching extension
    """
    if schema_editor.connection.vendor == 'postgresql':
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("create extension if not exists pg_trgm")


class Migration(migrations.Migration):
    """
    Attaches the functions for the migrations
    """
    dependencies = [
        ('api', '0090_fuel_code_status_set_effective_dates'),
    ]

    operations = [
        RunPython(
            add_trgrm_extension,
            reverse_code=None
        )
    ]
