# Generated by Django 2.2.5 on 2020-08-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_webapp_draw', '0006_auto_20200810_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='up_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]