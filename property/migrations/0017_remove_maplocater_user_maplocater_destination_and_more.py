# Generated by Django 4.1.4 on 2023-01-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_maplocater_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maplocater',
            name='user',
        ),
        migrations.AddField(
            model_name='maplocater',
            name='destination',
            field=models.CharField(default='Dewas', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maplocater',
            name='distance',
            field=models.DecimalField(decimal_places=2, default=120.36, max_digits=10),
            preserve_default=False,
        ),
    ]
