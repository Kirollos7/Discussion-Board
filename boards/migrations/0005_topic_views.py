# Generated by Django 3.0.7 on 2020-06-15 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20200613_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
