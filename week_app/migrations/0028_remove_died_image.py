# Generated by Django 4.2.7 on 2024-01-31 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week_app', '0027_died_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='died',
            name='image',
        ),
    ]
