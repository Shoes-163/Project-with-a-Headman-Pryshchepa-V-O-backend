# Generated by Django 5.2.3 on 2025-06-26 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_devices_is_working'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metrics',
            old_name='type_of_metrics',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='metrics',
            old_name='value_of_metrics',
            new_name='value',
        ),
    ]
