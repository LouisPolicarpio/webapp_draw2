from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class  User_images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    desc = models.CharField(max_length=300, null=True, blank=False)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)

    def __str__(self):
        return self.title


class Adjective(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word

class Verb(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word

class Adverb(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word
