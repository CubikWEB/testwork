# Generated by Django 4.0.1 on 2022-01-24 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testworkapp', '0004_alter_newslist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 24, 14, 9, 6, 276001), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 24, 14, 9, 6, 273999), verbose_name='Дата создания'),
        ),
    ]
