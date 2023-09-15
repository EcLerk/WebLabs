# Generated by Django 4.2.5 on 2023-09-14 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_rename_driver_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='email',
            field=models.EmailField(default='', max_length=254, validators=[django.core.validators.RegexValidator('/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i')], verbose_name='эл. почта'),
        ),
        migrations.AddField(
            model_name='employees',
            name='phone_number',
            field=models.CharField(default='+375441111111', max_length=13, validators=[django.core.validators.RegexValidator('^\\+375?\\d{9}$', "Phone number must be entered in the format: '+999999999'")], verbose_name='номер телефона'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position',
            field=models.CharField(default='', max_length=40, verbose_name='должность'),
        ),
    ]