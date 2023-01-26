from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    author = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    date = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.title
        
