# Generated by Django 5.0.6 on 2024-06-01 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shirinliklar',
            new_name='Drink',
        ),
        migrations.RenameModel(
            old_name='Ichimliklar',
            new_name='Sweet',
        ),
    ]
