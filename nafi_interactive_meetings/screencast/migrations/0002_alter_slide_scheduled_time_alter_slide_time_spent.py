# Generated by Django 5.0.6 on 2024-06-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screencast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='scheduled_time',
            field=models.TimeField(blank=True, default='00:05:00', verbose_name='Запланированное время на блок'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='time_spent',
            field=models.TimeField(blank=True, default='00:00:00', verbose_name='Потраченное время на блок'),
        ),
    ]
