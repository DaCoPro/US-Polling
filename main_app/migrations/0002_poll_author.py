# Generated by Django 3.1.2 on 2021-01-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='author',
            field=models.TextField(default=0, max_length=150),
        ),
    ]
