from django.db import models

# Create your models here.

from django.urls import reverse

class Notes(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()

    
    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('noteslist', kwargs = {"pk": self.pk})
