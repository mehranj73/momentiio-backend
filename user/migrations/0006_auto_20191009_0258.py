# Generated by Django 2.2.5 on 2019-10-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20191001_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
