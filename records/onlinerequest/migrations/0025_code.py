# Generated by Django 4.2.11 on 2024-04-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinerequest', '0024_requirement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=64)),
            ],
        ),
    ]
