# Generated by Django 4.2.7 on 2024-01-30 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week_app', '0012_rename_week_died_week_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='died',
            old_name='week_number',
            new_name='week',
        ),
    ]