# Generated by Django 4.2.5 on 2023-09-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_coupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]