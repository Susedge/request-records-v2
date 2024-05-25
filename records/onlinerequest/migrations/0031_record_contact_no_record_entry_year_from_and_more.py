# Generated by Django 4.2.11 on 2024-05-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinerequest', '0030_profile_contact_no_profile_entry_year_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='contact_no',
            field=models.CharField(default='09667614313', max_length=64),
        ),
        migrations.AddField(
            model_name='record',
            name='entry_year_from',
            field=models.IntegerField(default='2018'),
        ),
        migrations.AddField(
            model_name='record',
            name='entry_year_to',
            field=models.IntegerField(default='2024'),
        ),
        migrations.AddField(
            model_name='record',
            name='middle_name',
            field=models.CharField(default='De Guz Man', max_length=64),
        ),
    ]