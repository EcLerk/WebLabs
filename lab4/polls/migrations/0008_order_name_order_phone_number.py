# Generated by Django 4.2.1 on 2023-06-06 05:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='USER', max_length=20, verbose_name='имя'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='+375441111111', max_length=12, validators=[django.core.validators.RegexValidator('^\\+?375?\\d{9}$', "Phone number must be entered in the format: '+999999999'")], verbose_name='номер телефона'),
        ),
    ]
