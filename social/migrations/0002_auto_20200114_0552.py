# Generated by Django 2.2.8 on 2020-01-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=500),
            preserve_default=False,
        ),
    ]
