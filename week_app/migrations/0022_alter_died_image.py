# Generated by Django 4.2.7 on 2024-01-30 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('week_app', '0021_alter_died_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='died',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='week_app.image'),
        ),
    ]
