# Generated by Django 3.0.7 on 2020-06-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200613_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(help_text='Enter Your Subject', max_length=500, null=True),
        ),
    ]
