# Generated by Django 4.0.1 on 2022-01-25 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testworkapp', '0010_alter_backsaids_date_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backsaids',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='backsaids',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 12, 2, 18, 57025), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 12, 2, 18, 56027), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 12, 2, 18, 54025), verbose_name='Дата создания'),
        ),
    ]