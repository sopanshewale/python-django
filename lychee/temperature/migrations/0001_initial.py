# Generated by Django 2.0.5 on 2018-05-13 02:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.PositiveIntegerField(default=0, verbose_name='Current Temperatuer in Cel')),
                ('min_temp', models.PositiveIntegerField(default=0, verbose_name='Current Temperatuer in Cel')),
                ('max_temp', models.PositiveIntegerField(default=0, verbose_name='Current Temperatuer in Cel')),
                ('entry_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Entry Time')),
            ],
        ),
    ]
