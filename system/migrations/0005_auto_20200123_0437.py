# Generated by Django 2.2.8 on 2020-01-23 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to=system.models.image_path_generator, width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
