# Generated by Django 5.0.6 on 2024-06-19 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screencast', '0006_remove_slide_unique_order_per_event_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='slide',
            unique_together=set(),
        ),
    ]
