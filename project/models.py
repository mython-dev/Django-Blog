from django.db import models
from django.utils import timezone


# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True,default=timezone.now)

    def __str__(self) -> str:
        return self.title





