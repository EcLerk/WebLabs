# Generated by Django 4.2.5 on 2023-09-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_faq_answer_alter_faq_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='photo',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d'),
        ),
    ]
