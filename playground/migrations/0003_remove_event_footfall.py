# Generated by Django 4.1.7 on 2023-03-22 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_event_date_event_footfall_alter_event_starttime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='footfall',
        ),
    ]
