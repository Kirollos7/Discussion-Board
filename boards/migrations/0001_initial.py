# Generated by Django 3.0.7 on 2020-06-12 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Name of Category.', max_length=50, null=True, unique=True)),
                ('description', models.TextField(help_text='Enter Description of Category.', max_length=2000, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(help_text='Enter Your Subject', max_length=1000, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='boards.Board')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.Topic')),
            ],
        ),
    ]
