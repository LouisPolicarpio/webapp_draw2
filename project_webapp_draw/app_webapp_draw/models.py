from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class  User_images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    up_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='user_images', blank=False)

    def __str__(self):
        return self.title
