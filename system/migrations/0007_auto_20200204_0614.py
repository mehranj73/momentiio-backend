# Generated by Django 2.2.8 on 2020-02-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20200204_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='background',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='blend_mode',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='image_filter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='opacity',
            field=models.CharField(max_length=5, null=True),
        ),
    ]