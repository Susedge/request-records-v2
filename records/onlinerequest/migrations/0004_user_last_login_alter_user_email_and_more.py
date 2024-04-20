# Generated by Django 5.0.4 on 2024-04-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinerequest', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_number',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
