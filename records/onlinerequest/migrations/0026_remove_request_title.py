# Generated by Django 4.2.11 on 2024-04-30 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinerequest', '0025_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='title',
        ),
    ]