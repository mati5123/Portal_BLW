# Generated by Django 4.2.7 on 2024-01-29 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week_app', '0009_rename_content_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
