# Generated by Django 2.2.5 on 2020-08-12 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_webapp_draw', '0013_auto_20200812_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_images',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_images',
            name='desc',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='user_images',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user_images',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]