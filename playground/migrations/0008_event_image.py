# Generated by Django 4.1.7 on 2023-03-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0007_remove_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.URLField(default=None),
        ),
    ]
