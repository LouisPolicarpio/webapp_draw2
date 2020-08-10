from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class  User_images(models.Model):

    image = models.ImageField(upload_to='user_images', blank=False)


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
