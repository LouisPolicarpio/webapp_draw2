# Generated by Django 2.2.5 on 2020-08-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_webapp_draw', '0014_auto_20200812_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]