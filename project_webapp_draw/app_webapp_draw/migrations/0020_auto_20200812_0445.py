# Generated by Django 2.2.5 on 2020-08-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_webapp_draw', '0019_auto_20200812_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
