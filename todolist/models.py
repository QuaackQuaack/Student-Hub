from django.db import models

from django.urls import reverse
# Create your models here.

class Post(models.Model):
    task = models.CharField(max_length = 200)
    body = models.TextField()

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('home')
