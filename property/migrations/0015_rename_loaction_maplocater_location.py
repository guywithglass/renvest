# Generated by Django 4.1.4 on 2023-01-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_maplocater'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maplocater',
            old_name='loaction',
            new_name='location',
        ),
    ]
