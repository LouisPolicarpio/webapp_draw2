# Generated by Django 2.2.5 on 2020-08-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_webapp_draw', '0010_auto_20200810_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='image',
            field=models.ImageField(upload_to='user_images'),
        ),
    ]
