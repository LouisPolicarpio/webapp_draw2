# Generated by Django 2.2.5 on 2020-08-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_webapp_draw', '0016_auto_20200812_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='image',
            field=models.ImageField(upload_to='user_images'),
        ),
    ]
