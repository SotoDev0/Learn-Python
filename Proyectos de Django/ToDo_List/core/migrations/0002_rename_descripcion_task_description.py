# Generated by Django 5.1 on 2024-08-27 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripcion',
            new_name='description',
        ),
    ]
