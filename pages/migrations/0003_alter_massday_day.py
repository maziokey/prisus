# Generated by Django 3.2.9 on 2021-11-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_mass_massday_masstype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massday',
            name='day',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1),
        ),
    ]
