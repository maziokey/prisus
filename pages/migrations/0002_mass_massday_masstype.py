# Generated by Django 3.2.9 on 2021-11-09 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MassDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('MORN', 'Morning'), ('AFTN', 'Afternoon'), ('EVE', 'Evening'), ('MID', 'Midnight'), ('VIG', 'Vigil')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Mass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('mass_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parish_mass_days', to='pages.massday')),
                ('mass_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parish_mass_types', to='pages.masstype')),
                ('parish_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parish_masses', to='pages.parish')),
            ],
        ),
    ]
